#!/usr/bin/python3
"""this module conatins unittest for BaseModel class"""


import unittest
from models.base_model import BaseModel
from uuid import uuid4
import datetime


class TestBaseModel(unittest.TestCase):
    """This class will define methods which will
    use to test BaseModel class"""

    def setUP(self):
        """this method will run before every test"""
        base1 = BaseModel()

    def test_type(self):
        """this method will test types of attributes of
        BaseModel object is correct"""
        base1 = BaseModel()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime.datetime)
        self.assertEqual(type(base1.updated_at), datetime.datetime)
        self.assertEqual(type(str(base1)), str)
        self.assertEqual(type(base1.to_dict()), dict)

    def test_str(self):
        """this method will test __str__ will print the correct format
        of the object representation"""
        base1 = BaseModel()
        str1 = f'[BaseModel] {(base1.id)} {base1.__dict__}'
        self.assertEqual(str(base1), str1)

    def test_to_dict(self):
        """this method will test to_dict method will display the correct
        dictionary format and gives us the dictionaty representation"""
        base1 = BaseModel()
        dict1 = base1.__dict__.copy()
        dict1['__class__'] = 'BaseModel'
        dict1['created_at'] = base1.created_at.isoformat()
        dict1['updated_at'] = base1.updated_at.isoformat()
        dict2 = base1.to_dict()
        self.assertEqual(dict2, dict1)
        self.assertIn('__class__', dict2.keys())
        self.assertIn('id', dict2.keys())
        self.assertIn('created_at', dict2.keys())
        self.assertIn('updated_at', dict2.keys())
        self.asserEqual(type(dict2['id']), str)
        self.assertEqual(type(dict2['created_at']), str)
        self.assertEqual(type(dict2['updated_at']), str)
