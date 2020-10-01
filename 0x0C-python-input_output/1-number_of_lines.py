#!/usr/bin/python3
"""
Module 1-number_of_lines.py
"""


def number_of_lines(filename=""):
        """returns line number"""
        with open(filename, encoding="utf-8") as myFile:
            return len(myFile.readlines())
