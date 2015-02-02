# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


def update_profile(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-collective.geotransform:default')
