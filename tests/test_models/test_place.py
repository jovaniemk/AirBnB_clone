#!/usr/bin/python3
"""this module conatins unittest for Place class"""


import unittest
from models.place import Place
from uuid import uuid4
import datetime


class test_place(unittest.TestCase):
    """this class will contain methods which will test
    types and values of attributes of place"""

    def test_type(self):
        """this method will test wheter types of
        attributes are correct"""
        place1 = Place()
        self.assertEqual(type(place1.city_id), str)
        self.assertEqual(type(place1.user_id), str)
        self.assertEqual(type(place1.name), str)
        self.assertEqual(type(place1.description), str)
        self.assertEqual(type(place1.number_rooms), int)
        self.assertEqual(type(place1.number_bathrooms), int)
        self.assertEqual(type(place1.max_guest), int)
        self.assertEqual(type(place1.price_by_night), int)
        self.assertEqual(type(place1.latitude), float)
        self.assertEqual(type(place1.longitude), float)
        self.assertEqual(type(place1.amenity_ids), list)

    def test_value(self):
        """this method will test whether values of attributes
        are correct"""
        place1 = Place()
        self.assertEqual(place1.city_id, "")
        self.assertEqual(place1.user_id, "")
        self.assertEqual(place1.name, "")
        self.assertEqual(place1.description, "")
        self.assertEqual(place1.number_rooms, 0)
        self.assertEqual(place1.number_bathrooms, 0)
        self.assertEqual(place1.max_guest, 0)
        self.assertEqual(place1.price_by_night, 0)
        self.assertEqual(place1.latitude, 0.0)
        self.assertEqual(place1.longitude, 0.0)
        self.assertEqual(place1. amenity_ids, [])
