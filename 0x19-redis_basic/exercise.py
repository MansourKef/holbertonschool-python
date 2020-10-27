#!/usr/bin/env python3
"""
Module exercise.py
"""


import redis


class Cache:
    """
    Cache Class
    """
    def __init__(self):
        """
        init function
        """
        r = redis.Redis()
        self.__redis = r
        r.flushdb()

    def store(self, data):
        """
        store function
        """
        key = str(self.__redis.randomkey())
        self.__redis.set(key, data)
        return key
