# -*- coding: utf-8 -*-
from collective.gcs import message_factory as _
from zope import schema
from zope.interface import Interface


class IGcsLayer(Interface):
    """ Theme layer.
    """


class IGcsSettings(Interface):
    gcs_id = schema.TextLine(
        title=_(u'gcs_id_title', u'Google Custom Search ID'),
        description=_(
            u'gcs_id_help',
            default=u'ID, as available in the gcs control panel on google.com/cse.'  # noqa
        ),
        required=True,
    )
