#!/usr/bin/env python3
"""update topics"""


def update_topics(mongo_collection, name, topics):
    """changing topics of a document based on the name"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
