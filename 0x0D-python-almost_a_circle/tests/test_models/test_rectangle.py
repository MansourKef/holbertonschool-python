#!/usr/bin/python3
"""
Unittest for rectangle.py
"""


import unittest
import sys
from models.rectangle import Rectangle
from models.based import Base

class TestInit(unittest.TestCase):

    def test_area(self):
        #Test The init of the function based on id
        self.assertEqual(Rectangle.area(Rectangle(3, 2)), 6)
        self.assertEqual(Rectangle.area(Rectangle(2, 10)), 20)
        self.assertEqual(Rectangle.area(Rectangle(8, 7)), 56)
