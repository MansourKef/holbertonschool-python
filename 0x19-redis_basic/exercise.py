#!/usr/bin/env python3
"""
Module exercise.py
"""


import redis
from uuid import uuid4


class Cache:
    """
    Cache Class
    """
    def __init__(self):
        """
        init function
        """
        r = redis.Redis()
        self._redis = r
        self_redis.flushdb()

    def store(self, data):
        """
        store function
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
