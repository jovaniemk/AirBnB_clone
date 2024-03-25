#!/usr/bin/python3
"""this module conatins unittest for User class"""


import unittest
from models.user import User
from uuid import uuid4
import datetime


class test_user(unittest.TestCase):
    """this class contains these methods to test
    class User"""

    def test_type(self):
        """this method will test wheter the attributes of User are
        in their correct type"""
        user1 = User()
        self.assertEqual(type(user1.email), str)
        self.assertEqual(type(user1.password), str)
        self.assertEqual(type(user1.first_name), str)
        self.assertEqual(type(user1.last_name), str)
