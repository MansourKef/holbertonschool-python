#!/usr/bin/env python3
"""
Module exercise.py
"""


import redis
from uuid import uuid4
from typing import Union, Optional, Callable, List


class Cache:
    """
    Cache Class
    """
    def __init__(self) -> None:
        """
        init function
        """
        self._redis = redis.Redis()
        self_redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store function
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
