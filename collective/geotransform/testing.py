from plone.testing import z2
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import collective.geotransform


COLLECTIVE_GEOTRANSFORM_FIXTURE = PloneWithPackageLayer(
    name="COLLECTIVE_GEOTRANSFORM_FIXTURE",
    zcml_filename="configure.zcml",
    zcml_package=collective.geotransform,
    gs_profile_id="collective.geotransform:default")

COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GEOTRANSFORM_FIXTURE,),
    name="CollectiveGeotransform:Integration")

COLLECTIVE_GEOTRANSFORM_ROBOT_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_GEOTRANSFORM_FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="cpskin.core:Robot")
