#!/usr/bin/env python3
"""
Module 10-update_topics.py
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update_topics
    """
    return mongo_collection.update_many({"name": name}, {
        "$set": {"topics": topics}})
