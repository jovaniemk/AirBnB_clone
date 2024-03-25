#!/usr/bin/python3
"""this module conatins unittest for Review class"""


import unittest
from models.place import Review
from uuid import uuid4
import datetime


class test_review(unittest.TestCase):
    """this class will contain methods which will test
    types and values of attributes of Review class"""

    def test_type(self):
        """this method will test whether types of attributes
        are correct"""
        re1 = Review()
        self.assertEqual(type(re1.place_id), str)
        self.assertEqual(type(re1.user_id), str)
        self.assertEqual(type(re1.text), str)

    def test_values(self):
        """this method will test whether values of attributes
        are correct"""
        re1 = Review()
        self.assertEqual(type(re1.place_id), str)
        self.assertEqual(type(re1.user_id), str)
        self.assertEqual(type(re1.text), str)
