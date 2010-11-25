import re
import base64

from zope.interface import implements, Interface
from zope.component import adapts

from plone.transformchain.interfaces import ITransform

emailregex = r'\"mailto:["=]?(\b[A-Z0-9._%-]+@[A-Z0-9._%-]+\.[A-Z]{2,4}\b)\"'
emailRegexp = re.compile(emailregex, re.I | re.S | re.U)


def replaceEmail(match):
    """Replace email strings with mailto: links
    """
    url = match.groups()[0]
    url = base64.urlsafe_b64encode(url)
    return '"contact/%s" rel="nofollow"' % url


class emailObfuscatorTransform(object):
    implements(ITransform)
    adapts(Interface, Interface) # any context, any request
    order = 9000

    def __init__(self, published, request):
        self.published = published
        self.request = request

    def applyTransform(self):
        if 'Anonymous' in self.request['AUTHENTICATED_USER'].getUserName():
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
