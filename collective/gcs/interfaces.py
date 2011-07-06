from zope import schema
from zope.interface import Interface
from collective.gcs import messageFactory as _

class IGcsLayer(Interface):
    """ Theme layer.
    """

class IGcsSettings(Interface):

    gcs_id = schema.Text(
            title=_(u'gcs_id_title', u'Google Custom Search ID'),
            description=_(u'gcs_id_help',
                default=u'ID, as available in the gcs control panel.'),
            required=True
        )
