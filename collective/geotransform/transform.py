# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from collective.geotransform.interfaces import IGeoTransformLayer
from plone import api
from plone.transformchain.interfaces import ITransform
from zope.component import adapter
from zope.component.hooks import getSite
from zope.interface import Interface
from zope.interface import implementer

import base64
import re
import six

emailPattern = r"[A-Z0-9._%\+\-=:]+@[A-Z0-9._%\+\-=:]+\.[A-Z0-9._\+\-=:]+"
emailRegexp = re.compile(emailPattern, re.I | re.S | re.U)


def isNotInTextarea(str):
    return str.parent.name != "textarea"


def replaceMailTos(source):
    """
    Replace mailto href strings with encrypted geomailto href strings
    """
    soup = BeautifulSoup(source, 'lxml')
    mailtoTags = soup.select('a[href^="mailto:"]')
    for tag in mailtoTags:
        address = tag.get('href')[7:]
        if isinstance(address, six.text_type):
            # base64.b64encode needs bytes in py2 and py3
            address = address.encode('utf8')
        cryptedAddress = base64.b64encode(address)
        if six.PY3:
            # base64.b64encode returns bytes
            cryptedAddress = cryptedAddress.decode('utf8')
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
            if isinstance(mail, six.text_type):
                mail = mail.encode('utf8')
            encryptedMail = base64.b64encode(mail)
            if six.PY3:
                encryptedMail = encryptedMail.decode('utf8')
            newTag = soup.new_tag("span")
            newTag["class"] = "geomailaddress"
            newTag.string = encryptedMail
            replaced_text = text.replace(mail, str(newTag))
            text.replace_with(BeautifulSoup(replaced_text, "html.parser"))
    return str(soup)


@implementer(ITransform)
@adapter(Interface, Interface)  # any context, any request
class emailObfuscatorTransform(object):
    order = 9000

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def _cryptAllMails(self, source):
        result = replaceMailTos(source)
        result = replaceMails(result)
        if isinstance(result, six.text_type):
            result = result.encode('utf8')
        return result

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
        return self._cryptAllMails(result)

    def transformUnicode(self, result, encoding):
        if not self.applyTransform():
            return result
        return self._cryptAllMails(result)

    def transformIterable(self, result, encoding):
        if not self.applyTransform():
            return result
        return [self._cryptAllMails(r) for r in result]
