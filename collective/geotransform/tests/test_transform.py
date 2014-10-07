import unittest2 as unittest
from zope.component import queryMultiAdapter

from plone.transformchain.interfaces import ITransform

from collective.geotransform.testing import COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING


class TestTransform(unittest.TestCase):

    layer = COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_transform(self):
        request = self.layer['request']
        published = ''
        transformer = queryMultiAdapter((published, request,), ITransform,
                                        name=u'collective.geotransform')

        # Simple mail link
        mail = """<a href="mailto:me@me.com">Mail text</a>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)

        # Mail link with subject
        mail = """<a href="mailto:me@me.com?subject=Test">Mail text</a>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)

        # Mail link with subject and body
        mail = """<a href="mailto:me@me.com?subject=Test&amp;body=Test">Mail text</a>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)
