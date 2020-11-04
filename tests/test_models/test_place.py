#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test class Place"""

    @classmethod
    def test_setupPlace(cls):
        cls.place = Place()
        cls.place.city_id = "Tulsa"
        cls.place.user_id = "12345-67890"
        cls.place.name = "Holberton School"
        cls.place.description = "Hello, this is Holberton school."
        cls.place.number_rooms = 20
        cls.place.number_bathrooms = 3
        cls.place.max_guest = 100
        cls.place.price_by_night = 40
        cls.place.latitude = 36.1
        cls.place.longitude = 95.9
        cls.place.amenity_ids = ["09876-54321"]

    def test_Place_instance(self):
        """test if the obj is an inst of place, BaseModel
        """
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertIsInstance(obj, BaseModel)

    def test_Place_attr(self):
        place_obj = Place()
        self.assertIn("id", place_obj.__dict__)
        self.assertIn("created_at", place_obj.__dict__)
        self.assertIn("updated_at", place_obj.__dict__)
        self.assertIn("name", Place.__dict__)
        self.assertIn("city_id", Place.__dict__)
        self.assertIn("user_id", Place.__dict__)
        self.assertIn("description", Place.__dict__)
        self.assertIn("number_rooms", Place.__dict__)
        self.assertIn("number_bathrooms", Place.__dict__)
        self.assertIn("max_guest", Place.__dict__)
        self.assertIn("price_by_night", Place.__dict__)
        self.assertIn("latitude", Place.__dict__)
        self.assertIn("longitude", Place.__dict__)
        self.assertIn("amenity_ids", Place.__dict__)
        """test if attr in correct type"""
        self.assertEqual(type(place_obj.city_id), str)
        self.assertEqual(type(place_obj.user_id), str)
        self.assertEqual(type(place_obj.name), str)
        self.assertEqual(type(place_obj.description), str)
        self.assertEqual(type(place_obj.number_rooms), int)
        self.assertEqual(type(place_obj.number_bathrooms), int)
        self.assertEqual(type(place_obj.max_guest), int)
        self.assertEqual(type(place_obj.price_by_night), int)
        self.assertEqual(type(place_obj.latitude), float)
        self.assertEqual(type(place_obj.longitude), float)
        self.assertEqual(type(place_obj.amenity_ids), list)

    def test_place_to_save(self):
        """test if the save() works"""
        tmpobj = Place()
        tmpobj.save()
        self.assertNotEqual(tmpobj.created_at, tmpobj.updated_at)


if __name__ == "__main__":
    unittest.main()
