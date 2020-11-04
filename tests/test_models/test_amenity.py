#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test class Amenity"""

    @classmethod
    def test_setupAmenity(cls):
        cls.amenity = Amenity()
        cls.amenity.name = "cafe"

    def test_Amenity_instance(self):
        """test if the obj is an inst of amenity, BaseModel
        """
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertIsInstance(obj, BaseModel)

    def test_amenity_attr(self):
        amen_obj = Amenity()
        self.assertIn("id", amen_obj.__dict__)
        self.assertIn("created_at", amen_obj.__dict__)
        self.assertIn("updated_at", amen_obj.__dict__)
        self.assertIn('name', Amenity.__dict__)
        """test if attr in correct type"""
        self.assertEqual(type(amen_obj.name), str)

    def test_Amenity_to_save(self):
        """test if the save() works"""
        tmpobj = Amenity()
        tmpobj.save()
        self.assertNotEqual(tmpobj.created_at, tmpobj.updated_at)


if __name__ == "__main__":
    unittest.main()
