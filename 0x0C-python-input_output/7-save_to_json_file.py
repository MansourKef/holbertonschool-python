#!/usr/bin/python3
"""
Module 7
"""


import json


def save_to_json_file(my_obj, filename):

        """code object to Jason
        and write into a file
        """
        with open(filename, "w") as MyFile:
            json.dump(my_obj, MyFile)
