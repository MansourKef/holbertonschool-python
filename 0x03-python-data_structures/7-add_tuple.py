#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == () and tuple_b:
        return tuple_b
    if tuple_b == () and tuple_a:
        return tuple_a
    if len(tuple_a) >= 2 & len(tuple_b) >= 2:
        tuple_c = ("({}, {})".format(
            tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]))
    if len(tuple_a) == 1:
        tuple_c = ("({}, {})".format(tuple_a[0] + tuple_b[0], tuple_b[1]))
    if len(tuple_b) == 1:
        tuple_c = ("({}, {})".format(tuple_a[0] + tuple_b[0], tuple_a[1]))
    if len(tuple_a) == 0:
        tuple_c = tuple_b
    if len(tuple_b) == 0:
        tuple_c = tuple_a
    return tuple_c
