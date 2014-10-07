import re
import base64

from zope.interface import implements, Interface
from zope.component import adapts
from zope.component import getMultiAdapter
from zope.component.hooks import getSite
 
from plone.transformchain.interfaces import ITransform

emailregex = r'\"mailto:["=]?(\b[A-Z0-9._%-]+@[A-Z0-9._%-]+\.[A-Z]{2,4}\b)\"'
emailRegexp = re.compile(emailregex, re.I | re.S | re.U)


def replaceEmail(match):
    """Replace email strings with mailto: links
    """
    url = match.groups()[0]
    return '"contact/%s" rel="nofollow"' % url
    url = base64.b64encode(url)


class emailObfuscatorTransform(object):
    implements(ITransform)
    adapts(Interface, Interface) # any context, any request
    order = 9000

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def applyTransform(self):
        site = getSite()
        if not site:
            return False
        portal_state = getMultiAdapter((site , self.request), name=u"plone_portal_state")
        if portal_state.anonymous():
            return True
        else:
            return False

    def transformBytes(self, result, encoding):
        if self.applyTransform():
            return emailRegexp.subn(replaceEmail, result)[0]
        else:
            return None

    def transformUnicode(self, result, encoding):
        if self.applyTransform():
            return emailRegexp.subn(replaceEmail, result)[0]
        else:
            return None

    def transformIterable(self, result, encoding):
        if self.applyTransform():
            return [emailRegexp.subn(replaceEmail, r)[0] for r in result]
        else:
            return None
