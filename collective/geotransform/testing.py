from plone import api
from plone.testing import z2
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE

import collective.geotransform

TEXT = """
<h1>Contact me at me@me.com<h1>
<p>Lorem Ipsum dolor sit amet</p>
<a href="mailto:you@you.com">Contact you</a><br />
<a href="mailto:them@them.com?subject=supersub">Contact them</a><br />
"""


class GeoTransformPloneWithPackageLayer(PloneWithPackageLayer):

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.geotransform:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        doc = api.content.create(
            type='Document',
            title='Simple Document',
            id='simple-document',
            container=portal)
        doc.setText(TEXT)


COLLECTIVE_GEOTRANSFORM_FIXTURE = GeoTransformPloneWithPackageLayer(
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
