#!/usr/bin/python3
def inherits_from(obj, a_class):
    """check if the class of obj
     inhertid from a_class
     """
    if a_class == type(obj):
        return  False
    elif a_class in type(obj).mro():
        return True
    else:
        return  False
