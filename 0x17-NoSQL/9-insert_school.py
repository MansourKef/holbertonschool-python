#!/usr/bin/env python3
"""
Module 9-insert_school.py
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert_school
    """
    mongo_collection.insert({name: kwargs['name'], address: kwargs['address']})
    return mongo_collection.find({name: kwargs['name']}, {
        "_id": 1, "name": 0, "address": 0})
