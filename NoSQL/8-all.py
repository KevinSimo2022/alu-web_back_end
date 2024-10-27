#!/usr/bin/env python3
""" all """


def list_all(mongo_collection):
    """ all """
    documents = mongo_collection.find()
    return documents
