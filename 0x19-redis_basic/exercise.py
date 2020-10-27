#!/usr/bin/env python3
"""
Module exercise.py
"""


import redis
from uuid import uuid4
from typing import Union, Optional, Callable, List
from sys import byteorder
from functools import wraps


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

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[str, bytes, int, float]:
        """get method"""
        result = self._redis.get(key)
        return fn(result) if fn else result
