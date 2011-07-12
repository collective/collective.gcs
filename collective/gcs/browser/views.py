from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase


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
