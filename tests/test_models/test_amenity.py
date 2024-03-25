#!/usr/bin/python3
"""this module conatins unittest for Amenity class"""


import unittest
from models.amenity import Amenity
from uuid import uuid4
import datetime


class test_amenity(unittest.TestCase):
    """this class will contain methods which will
    test the types and values of attributes of
    Amenity class"""

    def test_type(self):
        """this method will test the types of Amenity
        attributes are correct in their type"""
        a1 = Amenity()
        self.assertEqual(type(a1.name), str)

    def test_value(self):
    """this method will test the types of Amenity
    attributes are correct in their type"""
    a1 = Amenity()
    self.assertEqual(a1.name, str)
