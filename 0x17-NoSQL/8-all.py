#!/usr/bin/env python3
"""
Module 8-all.py
"""


import pymongo


def list_all(mongo_collection):
    """
    list_all
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
