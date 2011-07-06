from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implements

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from cornerstone.browser.base import XBrowserView
from cornerstone.browser.renderer import RendererBase

class IGcsInfo(Interface):
    """View interface for Google Custom Search.
    """
    resultpage = Attribute(u"The link to the resultpage")

class GcsInfo(XBrowserView):
    implements(IGcsInfo)

    @property
    def resultpage(self):
        return self.makeUrl(self.context, resource=u'@@gcssearchresults')

class GcsView(GcsInfo):
    pass

class GcsSearchbox(ViewletBase, GcsInfo):
    render = ViewPageTemplateFile('searchbox.pt')

class GcsDevSearch(RendererBase, GcsInfo):

    def update(self):
        pass

    def render(self):
        return self.context.restrictedTraverse('@@gcsdevsearch')()
