#!/usr/bin/python3
"""
    100-singly_linked_list.py
    Modules Defines Node Class
"""


class Node():
    """This is An Square Class Based On The
    Square Class"""
    def __init__(self, data, next_node=None):
        """This is init function of this Class
        that sets the Value of data And next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets The Value Of The __data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets The Value Of The __data Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__size = value

    @property
    def next_node(self):
        """Gets The Value Of The __next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets The Value Of The __next_node Based On Some conditions"""
        if not value == [None] and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList():
    """
        100-singly_linked_list.py
        Modules Defines SinglyLinkedList
    """


    def __init__(self):
        """This is init function of this Class
        that sets the Value of __head"""
        self.__head = Node(0)

    def sorted_insert(self, value):
        """Function To Append The Nodes"""
        self.__head.add(value)
        self.__head.sort()
