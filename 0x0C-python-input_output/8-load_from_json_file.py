#!/usr/bin/python3
"""
Module 8
"""


import json


def load_from_json_file(filename):

        """
        crete object from jason file
        """
        with open(filename, "r") as MyFile:
            return json.load(MyFile)
