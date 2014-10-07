from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting

import collective.geotransform


COLLECTIVE_GEOTRANSFORM_FIXTURE = PloneWithPackageLayer(
    name="COLLECTIVE_GEOTRANSFORM_FIXTURE",
    zcml_filename="configure.zcml",
    zcml_package=collective.geotransform,
    gs_profile_id="collective.geotransform:default")

COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GEOTRANSFORM_FIXTURE,),
    name="CollectiveGeotransform:Integration")
