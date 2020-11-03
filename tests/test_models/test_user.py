#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Tests User Class"""

    @classmethod
    def test_setupUser(cls):
        cls.user = User()
        cls.user.email = "betty2020@holberton.com"
        cls.user.password = "mypassword"
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"

    def test_User_instance(self):
        """test if the obj is an instance of User, BaseModel
        """
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertIsInstance(obj, BaseModel)

    def test_User_attr(self):
        """tests User attributes"""
        user_obj = User()
        self.assertIn("id", user_obj.__dict__)
        self.assertIn("created_at", user_obj.__dict__)
        self.assertIn("updated_at", user_obj.__dict__)
        self.assertIn("email", User.__dict__)
        self.assertIn("password", User.__dict__)
        self.assertIn("first_name", User.__dict__)
        self.assertIn("last_name", User.__dict__)
        """test if attr in correct type"""
        self.assertEqual(type(user_obj.email), str)
        self.assertEqual(type(user_obj.password), str)
        self.assertEqual(type(user_obj.first_name), str)
        self.assertEqual(type(user_obj.first_name), str)

    def test_User_to_save(self):
        """test if the save() works"""
        tmpobj = User()
        tmpobj.save()
        self.assertNotEqual(tmpobj.created_at, tmpobj.updated_at)


if __name__ == "__main__":
    unittest.main()
