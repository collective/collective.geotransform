from collective.geotransform.testing import COLLECTIVE_GEOTRANSFORM_ROBOT_TESTING
from plone.testing import layered

import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests(
        [
            layered(
                robotsuite.RobotTestSuite("robot"),
                layer=COLLECTIVE_GEOTRANSFORM_ROBOT_TESTING,
            ),
        ]
    )
    return suite
