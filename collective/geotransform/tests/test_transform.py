# -*- coding: utf-8 -*-
import re
import unittest
from zope.component import queryMultiAdapter

from plone.app.testing import logout
from plone.transformchain.interfaces import ITransform

from collective.geotransform.testing import COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING


class TestTransform(unittest.TestCase):

    layer = COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testMailtoTransform(self):
        logout()
        published = ''
        request = self.layer['request']
        request.response['content-type'] = 'text/html;charset=utf-8'
        transformer = queryMultiAdapter((published, request,), ITransform,
                                        name=u'collective.geotransform')

        obfuscated_re = r'<html><body><a href="geomailto:(.)*" rel="nofollow">Mail text</a></body></html>'

        # Simple mail link
        mail = """<html><body><a href="mailto:me@me.com">Mail text</a></body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)
        self.assertTrue(re.match(obfuscated_re, obfuscatedMail))

        # Mail link with subject
        mail = """<html><body><a href="mailto:me@me.com?subject=Test">Mail text</a></body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)
        self.assertTrue(re.match(obfuscated_re, obfuscatedMail))

        # Mail link with subject and body
        mail = """<html><body><a href="mailto:me@me.com?subject=Test&amp;body=Test">Mail text</a></body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)
        self.assertTrue(re.match(obfuscated_re, obfuscatedMail))

    def testPlainMailTransform(self):
        logout()
        published = ''
        request = self.layer['request']
        request.response['content-type'] = 'text/html;charset=utf-8'
        transformer = queryMultiAdapter((published, request,), ITransform,
                                        name=u'collective.geotransform')

        # Simple mail address in content
        obfuscated_re = r'<html><body><span class="geomailaddress">(.)*</span></body></html>'
        mail = """<html><body>me@me.com</body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)
        self.assertTrue(re.match(obfuscated_re, obfuscatedMail))

        # Multiple mail addresses in content
        obfuscated_re = r'<html><body><h2><span class="geomailaddress">(.)*</span></h2><span class="geomailaddress">(.)*</span></body></html>'
        mail = """<html><body><h2>me@me.com</h2>you@you.com</body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)
        self.assertTrue(re.match(obfuscated_re, obfuscatedMail))

    def testLoggedInTransform(self):
        published = ''
        request = self.layer['request']
        request.response['content-type'] = 'text/html;charset=utf-8'
        transformer = queryMultiAdapter((published, request,), ITransform,
                                        name=u'collective.geotransform')

        mail = """<html><body><a href="mailto:me@me.com">Mail text</a></body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failUnless(mail == obfuscatedMail)

        mail = """<html><body>me@me.com</body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failUnless(mail == obfuscatedMail)

    def testInputsTransform(self):
        published = ''
        request = self.layer['request']
        request.response['content-type'] = 'text/html;charset=utf-8'
        transformer = queryMultiAdapter((published, request,), ITransform,
                                        name=u'collective.geotransform')

        mail = """<html><body><input value="mailto:me@me.com" />"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failUnless(mail == obfuscatedMail)

        mail = """<html><body><textarea>me@me.com</textarea></body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failUnless(mail == obfuscatedMail)

    def testNonHTMLTransform(self):
        published = ''
        request = self.layer['request']
        request.response['content-type'] = 'text/css;charset=utf-8'
        transformer = queryMultiAdapter((published, request,), ITransform,
                                        name=u'collective.geotransform')

        mail = """<html><body><a href="mailto:me@me.com">Mail text</a></body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failUnless(mail == obfuscatedMail)

    def testAccentMailTransoform(self):
        logout()
        published = ''
        request = self.layer['request']
        request.response['content-type'] = 'text/html;charset=utf-8'
        transformer = queryMultiAdapter((published, request,), ITransform,
                                        name=u'collective.geotransform')

        obfuscated_re = r'<html><body><a href="geomailto:(.)*" rel="nofollow">Mail text</a></body></html>'

        # Simple mail link
        mail = """<html><body><a href="mailto:mé@me.com">Mail text</a></body></html>"""
        obfuscatedMail = transformer.transformBytes(mail, 'utf-8')
        self.failIf(mail == obfuscatedMail)
        self.assertTrue(re.match(obfuscated_re, obfuscatedMail))

