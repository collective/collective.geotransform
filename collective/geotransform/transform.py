# -*- coding: utf-8 -*-
import re
import base64
from bs4 import BeautifulSoup
from collective.geotransform.interfaces import IGeoTransformLayer
from plone import api

from zope.interface import implements, Interface
from zope.component import adapts
from zope.component.hooks import getSite

from plone.transformchain.interfaces import ITransform

emailPattern = r"[A-Z0-9._%\+\-=:]+@[A-Z0-9._%\+\-=:]+\.[A-Z0-9._\+\-=:]+"
emailRegexp = re.compile(emailPattern, re.I | re.S | re.U)


def isNotInTextarea(str):
    return str.parent.name != "textarea"


def replaceMailTos(source):
    """
    Replace mailto href strings with encrypted geomailto href strings
    """
    soup = BeautifulSoup(source, 'lxml')
    mailtoTags = soup.select('a[href^=mailto:]')
    for tag in mailtoTags:
        address = tag.get('href')[7:]
        try:
            cryptedAddress = base64.b64encode(address)
        except UnicodeEncodeError:
            cryptedAddress = base64.b64encode(address.encode('utf8'))
        tag['href'] = "geomailto:%s" % cryptedAddress
        tag['rel'] = "nofollow"
    return str(soup)


def replaceMails(source):
    """
    Replace email strings with encrypted <span>
    """
    soup = BeautifulSoup(source, "lxml")
    texts = soup.find_all(string=isNotInTextarea)
    for text in texts:
        mails = emailRegexp.findall(text)
        for mail in mails:
            encryptedMail = base64.b64encode(mail)
            newTag = soup.new_tag("span")
            newTag["class"] = "geomailaddress"
            newTag.string = encryptedMail
            replaced_text = text.replace(mail, str(newTag))
            text.replace_with(BeautifulSoup(replaced_text, "html.parser"))
    return str(soup)


def cryptAllMails(source):
    result = replaceMailTos(source)
    result = replaceMails(result)
    return result


class emailObfuscatorTransform(object):
    implements(ITransform)
    adapts(Interface, Interface)  # any context, any request
    order = 9000

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def applyTransform(self):
        site = getSite()
        if not site:
            return False
        if not IGeoTransformLayer.providedBy(self.request):
            return False
        responseType = self.request.response.getHeader('content-type') or ''
        if not responseType.startswith(('text/html', 'text/xhtml')):
            return False
        if self.request.getHeader('X-Requested-With', '') == 'XMLHttpRequest':
            return False
        return api.user.is_anonymous()

    def transformBytes(self, result, encoding):
        if not self.applyTransform():
            return result
        return cryptAllMails(result)

    def transformUnicode(self, result, encoding):
        if not self.applyTransform():
            return result
        return cryptAllMails(result)

    def transformIterable(self, result, encoding):
        if not self.applyTransform():
            return result
        return [cryptAllMails(r) for r in result]
