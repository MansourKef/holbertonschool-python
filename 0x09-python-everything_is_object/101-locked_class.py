#!/usr/bin/python3
class LockedClass:
    """
    Class That prevents the cretaion of the instance
    unless its is with first_name only
    """
    __slots__ = ['first_name']

