#!/usr/bin/python3
"""
Module 4-append_write.py
"""


def append_write(filename="", text=""):
        """write and append a text in a file"""
        with open(filename, mode="a", encoding="utf-8") as myFile:
            return(myFile.write(text))
