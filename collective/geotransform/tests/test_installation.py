import unittest

from plone.app.testing import applyProfile

from collective.geotransform.testing import COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING
from collective.geotransform.interfaces import IGeoTransformLayer


class TestProfiles(unittest.TestCase):

    layer = COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING

    def test_layer(self):
        assert IGeoTransformLayer.providedBy(self.layer['request'])
