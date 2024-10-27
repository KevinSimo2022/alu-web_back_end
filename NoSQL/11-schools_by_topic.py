#!/usr/bin/env python3
"""school by topic"""


def schools_by_topic(mongo_collection, topic):
    """returning a list of schools having a certain topic"""
    return mongo_collection.find({"topics": topic})
