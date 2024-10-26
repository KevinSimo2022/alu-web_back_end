#!/usr/bin/env python3
""" insert school
"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
