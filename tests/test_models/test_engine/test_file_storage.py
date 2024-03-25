#!/usr/bin/python3
"""this module contains unit testing class
for the class FileStorage class"""


import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class test_file_storage(unittest.TestCase):
    """this class will contain test methods which
    will test the attributes and methods of FileStorage
    class"""

    def test_type(self):
        """this method will test the types of attributes are
        correct"""
        f1 = FileStorage()
        self.assertEqual(type(f1._FileStorage__file_path), str)
        self.assertEqual(type(f1._FileStorage__objects), dict)

    def test_values(self):
        """this method will test the values of attributes are
        correct"""
        f1 = FileStorage()
        self.assertEqual(f1._FileStorage__file_path, "file.json")

    def test_all(self):
        """this method will check wheter the all method of
        FileStorage class returns dictionary"""
        f1 = FileStorage()
        self.assertEqual(type(f1.all()), dict)

    def test_new(self):
        """this method will check whether new method of FileStorage
        class add new object to the dictionary"""
        f1 = FileStorage()
        base1 = BaseModel()
        str1 = f'BaseModel.{base1.id}'
        f1.new(base1)
        self.assertIn(str1, f1.all().keys())

    def test_save(self):
        """this method will check whether the save method saves
        the json serialization of te object"""
        f1 = FileStorage()
        f1.save()
        self.assertTrue(os.path.isfile(f1._FileStorage__file_path))
        self.assertTrue(os.path.getsize(f1._FileStorage__file_path)
                        > 0)

    def test_reload(self):
        """this method will check whether the reload method
        returns object representation of a class"""
        f1 = FileStorage()
        base1 = BaseModel()
        f1.new(base1)
        dict1 = f1.all()
        f1.save()
        f1.reload()
        dict2 = f1.all()
        self.assertEqual(dict1, dict2)
