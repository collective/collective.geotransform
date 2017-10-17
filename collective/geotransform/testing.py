from plone import api
from plone.testing import z2
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.textfield.value import RichTextValue

import transaction

TEXT = """
<h1>Contact me at me@me.com<h1>
<p>Lorem Ipsum dolor sit amet</p>
<a href="mailto:you@you.com">Contact you</a><br />
<a href="mailto:them@them.com?subject=supersub">Contact them</a><br />
<input id="mail-input" type="text" value="input@other.com" />
<textarea id="mail-textarea">textarea@other.com</textarea>
"""


def remove_inputs_tag_filtering(portal):
    pc = api.portal.get_tool(name='portal_transforms')
    transform = getattr(pc, 'safe_html')
    key = 'valid_tags'
    tags = transform.get_parameter_value(key)
    kwargs = {}
    kwargs[key + '_key'] = tags.keys() + ['input', 'textarea']
    kwargs[key + '_value'] = [str(s) for s in tags.values()] + ['1', '1']
    transform.set_parameters(**kwargs)
    transform._p_changed = True
    transform.reload()


class GeoTransformPackageLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        import collective.geotransform
        self.loadZCML(package=collective.geotransform)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.geotransform:default')
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        # we need to allow inputs tags for our robot tests
        remove_inputs_tag_filtering(portal)
        doc = api.content.create(
            type='Document',
            title='Simple Document',
            id='simple-document',
            container=portal,
        )
        doc.text = RichTextValue(
            TEXT,
            'text/html',
            'text/html',
        )
        api.content.transition(doc, 'publish')
        doc.reindexObject()
        transaction.commit()


COLLECTIVE_GEOTRANSFORM_FIXTURE = GeoTransformPackageLayer()


COLLECTIVE_GEOTRANSFORM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_GEOTRANSFORM_FIXTURE,),
    name="CollectiveGeotransform:Integration")

COLLECTIVE_GEOTRANSFORM_ROBOT_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_GEOTRANSFORM_FIXTURE,
           z2.ZSERVER_FIXTURE),
    name="CollectiveGeotransform:Robot")
