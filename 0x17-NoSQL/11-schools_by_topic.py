#!/usr/bin/env python3
"""
Module 11-schools_by_topic.py
"""


import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    schools_by_topic
    """
    return mongo_collection.find({"topics": topic})
