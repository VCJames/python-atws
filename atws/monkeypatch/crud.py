'''
Created on 17 Oct 2015

@author: matt
'''
from atws import query
from atws.helpers import get_entity_type,copy_attributes
from __init__ import monkey_patch


def mp_update(entity):
    result = entity._wrapper.update(entity)
    copy_attributes(result[0],entity)
    return True


def mp_delete(entity):
    entity._wrapper.delete(entity)
    return True


def mp_reload(entity):
    query = query.Query(get_entity_type(entity))
    query.WHERE('id',query.Equals,entity.id)
    result = entity._wrapper.query(query)
    copy_attributes(result[0],entity)
    return True
    

def mp_create(entity):
    result = entity._wrapper.create(entity)
    copy_attributes(result[0],entity)
    return True
    
generic_patches = {
                   'create':mp_create,
                   'reload':mp_reload,
                   'update':mp_update,
                   'delete':mp_delete
                   }
monkey_patch.add_generic_patches(generic_patches)
