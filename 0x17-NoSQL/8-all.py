#!/usr/bin/python3
"""
Module 8-all.py
"""


import pymongo


def list_all(mongo_collection):
    """
    list_all
    """
    if len(mongo_collection) == 0:
        return([])
    return mongo_collection.find()
