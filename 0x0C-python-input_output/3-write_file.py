#!/usr/bin/python3
"""
Module 3-write_file.py
"""


def write_file(filename="", text=""):
        """write a text in a file"""
        with open(filename, mode="w", encoding="utf-8") as myFile:
            return(myFile.write(text))
