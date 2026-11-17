from collective.geotransform.interfaces import IGeoTransformLayer
from collective.geotransform.testing import COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING

import unittest


class TestProfiles(unittest.TestCase):

    layer = COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING

    def test_layer(self):
        assert IGeoTransformLayer.providedBy(self.layer["request"])
