#!/usr/bin/env python3
"""
Module 9-insert_school.py
"""


import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert_school
    """
    return mongo_collection.insert_one(kwargs).inserted_id
