# -*- coding: utf-8 -*-
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getUtility


class GcsBase(object):

    @property
    def gcs_id(self):
        registry = getUtility(IRegistry)
        if 'collective.gcs.gcs_id' in registry:
            return registry['collective.gcs.gcs_id']
        return None


class GcsView(BrowserView, GcsBase):
    pass


class GcsSearchbox(ViewletBase, GcsBase):
    render = ViewPageTemplateFile('searchbox.pt')
