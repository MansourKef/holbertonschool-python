#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if i == len(str) - 1:
            print(chr(ord(str[i]) - 32), end="\n")
        else:
            print(chr(ord(str[i]) - 32), end="")
