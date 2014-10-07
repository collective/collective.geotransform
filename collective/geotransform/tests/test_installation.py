import unittest2 as unittest

from plone.app.testing import applyProfile

from collective.geotransform.testing import COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING


class TestProfiles(unittest.TestCase):

    layer = COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installation(self):
        portal = self.layer['portal']
        applyProfile(portal, 'collective.geotransform:default')
