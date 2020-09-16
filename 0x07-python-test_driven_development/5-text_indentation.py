#!/usr/bin/python3
"""
    5-text_indentation.py
    that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        print()
    for char in text:
        if not char == " ":
            if not char in(".", "?", ":"):
                print(char, end="")
            else:
                print(char)
                print()
