#!/usr/bin/python3
"""
Module 0-read_file.py
"""


def read_file(filename=""):
        """reads a file in UTF8"""
        with open(filename, encoding="utf-8") as myFile:
            print(myFile.read())
