#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests BaseModel Class"""

    def test_BaseModel_method(self):
        """Test if BaseModel has all methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_BaseModel_init(self):
        """tests init method"""
        test_obj = BaseModel()
        self.assertTrue(isinstance(test_obj, BaseModel))
        """test if the object is an instance of BaseModel"""
        self.assertIsInstance(test_obj, BaseModel)
        """test if BaseModel has all attributes"""
        self.assertIn("id", test_obj.__dict__)
        self.assertIn("created_at", test_obj.__dict__)
        self.assertIn("updated_at", test_obj.__dict__)
        """test if dictionaries contains all attr in correct type"""
        self.assertIsInstance(test_obj.id, str)
        self.assertIsInstance(test_obj.created_at, datetime)
        self.assertIsInstance(test_obj.updated_at, datetime)

    def test_BaseModel_save(self):
        """test if the save() works"""
        base_save = BaseModel()
        obj1 = base_save.updated_at
        base_save.save()
        obj2 = base_save.updated_at
        self.assertNotEqual(obj1, obj2)

    def test_BaseModel_todict(self):
        """test if the to_dict() works"""
        base_dict = BaseModel()
        obj_dict = base_dict.to_dict()
        self.assertEqual(base_dict.__class__.__name__, 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_output_str(self):
        str_dict = BaseModel()
        self.assertIsInstance(str_dict.__str__(), str)
        new_str_dict = BaseModel()
        str_output = "[{}] ({}) {}".format(
                new_str_dict.__class__.__name__,
                new_str_dict.id,
                new_str_dict.__dict__)
        self.assertEqual(str_output, new_str_dict.__str__())

if __name__ == "__main__":
    unittest.main()
