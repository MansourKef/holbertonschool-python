#!/usr/bin/python3
"""
Module 2-read_lines.py
"""


def read_lines(filename="", nb_lines=0):
        """reads n lines of a file in UTF8"""
        with open(filename, encoding="utf-8") as myFile:
            if nb_lines <=0:
                print(myFile.read())
            elif nb_lines >= len(myFile.readlines()):
                print(myFile.read())
            else:
                for i in range(nb_lines):
                    myFile.readline()
