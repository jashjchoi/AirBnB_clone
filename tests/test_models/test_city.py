#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test class City"""

    @classmethod
    def test_setupCity(cls):
        cls.city = City()
        cls.city.name = "Tulsa"
        cls.city.state_id = "OK"

    def test_City_instance(self):
        """test if the obj is an inst of City, BaseModel
        """
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertIsInstance(obj, BaseModel)

    def test_city_attr(self):
        city_obj = City()
        self.assertIn("id", city_obj.__dict__)
        self.assertIn("created_at", city_obj.__dict__)
        self.assertIn("updated_at", city_obj.__dict__)
        self.assertIn("name", City.__dict__)
        self.assertIn("state_id", City.__dict__)
        """test if attr in correct type"""
        self.assertEqual(type(city_obj.name), str)
        self.assertEqual(type(city_obj.state_id), str)

    def test_City_to_save(self):
        """test if the save() works"""
        tmpobj = City()
        tmpobj.save()
        self.assertNotEqual(tmpobj.created_at, tmpobj.updated_at)


if __name__ == "__main__":
    unittest.main()
