# -*- coding: utf-8 -*-
import re
import base64
from bs4 import BeautifulSoup
from collective.geotransform.interfaces import IGeoTransformLayer
from plone import api

from zope.interface import implementer
from zope.interface import Interface
from zope.component import adapter
from zope.component.hooks import getSite

from plone.transformchain.interfaces import ITransform

emailPattern = r"([A-Z0-9._%\+\-=:]+@[A-Z0-9._%\+\-=:]+\.[A-Z0-9._\+\-=:]+)|(<textarea.*?<\/textarea>|value=.*?>)"  # noqa
emailRegexp = re.compile(emailPattern, re.I | re.S | re.U)


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


def replaceMails(match):
    """
    Replace email strings with encrypted <span>
    """
    mail = match.groups()[0]
    if mail is not None:
        encryptedMail = base64.b64encode(mail)
        return """<span class="geomailaddress">%s</span>""" % encryptedMail
    else:
        return match.groups()[1]


@implementer(ITransform)
@adapter(Interface, Interface)  # any context, any request
class emailObfuscatorTransform(object):

    order = 9000

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def _cryptAllMails(self, source):
        result = replaceMailTos(source)
        return emailRegexp.sub(replaceMails, result)

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
        return self.transformBytes(result, encoding)

    def transformIterable(self, result, encoding):
        if not self.applyTransform():
            return result
        return [self._cryptAllMails(r) for r in result]
