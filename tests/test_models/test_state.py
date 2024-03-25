#!/usr/bin/python3
"""this module conatins unittest for state class"""


import unittest
from models.state import State
from uuid import uuid4
import datetime


class test_state(unittest.TestCase):
    """this class contains these methods to test
    class State"""

    def test_type(self):
        """this method will test wheter the attributes of State are
        in their correct type"""
        state1 = State()
        self.assertEqual(type(state1.name), str)

    def test_value(self):
        """this method will test wheter the attributes of State are
        empty at the intialization"""
        state1 = State()
        self.assertEqual(state1.name, "")
