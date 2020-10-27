#!/usr/bin/python3
"""
Module 0-basic_cache.py
"""


class BasicCache(BaseCaching):
    """
    BasicCache Class
    """
    def put(self, key, item):
        """
        Assign Values To Dict
        """
        if key and item:
            self.cache_data.append(key, item)

    def get(self, key):
        """
        Get Values From Dict
        """
        return self.cache_data(key)
