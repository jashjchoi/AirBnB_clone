#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test class State"""

    @classmethod
    def test_setupState(cls):
        cls.state = State()
        cls.state.state_id = "OK"

    def test_State_instance(self):
        """test if the obj is an inst of State, BaseModel
        """
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertIsInstance(obj, BaseModel)

    def test_State_attr(self):
        state_obj = State()
        self.assertIn("id", state_obj.__dict__)
        self.assertIn("created_at", state_obj.__dict__)
        self.assertIn("updated_at", state_obj.__dict__)
        self.assertIn("name", State.__dict__)
        """test if attr in correct type"""
        self.assertEqual(type(state_obj.name), str)

    def test_State_to_save(self):
        """test if the save() works"""
        tmpobj = State()
        tmpobj.save()
        self.assertNotEqual(tmpobj.created_at, tmpobj.updated_at)


if __name__ == "__main__":
    unittest.main()
