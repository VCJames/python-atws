'''
Created on 10 Jan 2016

@author: matt
'''
import logging
import pytz
import atws.monkeypatch.asdict
from datetime import datetime
from __init__ import monkey_patch
from atws.helpers import localise_datetime
from decimal import Decimal

logger = logging.getLogger(__name__)
UTC = pytz.timezone('UTC')

MARSHAL_MAP = {}


def datetime_to_utc_isoformat(dt):
    return localise_datetime(dt).astimezone(UTC).isoformat()


def convert(obj):
    result = {}
    for k,v in obj.iteritems():
        if type(v) == list:
            result[k] = []
            for d in v:
                result[k].append(convert(d))
        else:
            result[k] = convert_value(v)
    logger.debug('returning the following dictionary as marshallable')
    logger.debug(result)
    return result


def convert_value(v):
    if isinstance(v, datetime):
        try:
            return datetime_to_utc_isoformat(v)
        except AttributeError:
            return v
    if isinstance(v, basestring):
        try:
            return str(v)
        except TypeError:
            return v
    if isinstance(v, Decimal):
        return str(v)
    return v


def get_marshallable_dict(entity):
    e = entity.asdict()
    return convert(e)


generic_patches = {
   'asmarshallabledict':get_marshallable_dict,
   'asserializabledict':get_marshallable_dict
   }

monkey_patch.add_generic_patches(generic_patches)