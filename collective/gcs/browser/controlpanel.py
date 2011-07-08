from plone.app.registry.browser import controlpanel
from collective.gcs import message_factory as _
from collective.gcs.interfaces import IGcsSettings


class GcsControlPanelEditForm(controlpanel.RegistryEditForm):
    schema = IGcsSettings
    schema_prefix = 'collective.gcs'

    label = _(u"Google Custom Search settings")
    description = _(u"help_event_settings",
            default=u"Settings related to the Custom Search tool by Google.")

    def updateFields(self):
        super(GcsControlPanelEditForm, self).updateFields()

    def updateWidgets(self):
        super(GcsControlPanelEditForm, self).updateWidgets()


class GcsSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = GcsControlPanelEditForm
