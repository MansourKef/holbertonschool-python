#!/usr/bin/python3
"""
Unittest for max_integer([..])

"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """Test When List Values Are in correct Form"""
        self.assertAlmostEquals(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEquals(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEquals(max_integer([]), None)

    def test_values(self):
        """Test If The Values Are in Correct Form"""
        self.assertRaises(ValueError, max_integer, [1, "s", 3, 4])
        self.assertRaises(ValueError, max_integer, [1, 2, 4.1, 2])
        self.assertRaises(ValueError, max_integer, None)
