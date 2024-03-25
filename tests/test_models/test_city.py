#!/usr/bin/python3
"""this module conatins unittest for User class"""


import unittest
from models.city import City
from uuid import uuid4
import datetime


class test_city(unittest.TestCase):
    """this class will contain methods which will
    test for the class city"""

    def test_type(self):
        """this method will contain the types of
        atributes are correct"""
        city1 = City()
        self.assertEqual(type(city1.state_id), str)
        self.assertEqual(type(city1.name), str)

    def test_value(self):
        """this method will test the attributes
        are empty string"""
        city1 = City()
        self.assertEqual(city1.state_id, "")
        self.assertEqual(city1.name, "")
