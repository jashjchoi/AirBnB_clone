#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorageClass(unittest.TestCase):
    """ Tests FileStorage class """

    def check_inst(self):
        self.assertisInstance(storage, FileStorage)

    def check_attr(self):
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def test_all(self):
        all_storage = FileStorage()
        objs = all_storage.all()
        self.assertIsNotNone(objs)
        """tests if all() returns dictionary"""
        self.assertEqual(type(objs), dict)
        self.assertIs(objs, all_storage._FileStorage__objects)

    def test_storage_new_BaseModel(self):
        """create new storage instance of BaseModel"""
        new_bm = BaseModel()
        storage.new(new_bm)
        """tests if the dictionary is successfully added to BaseModel"""
        self.assertIn("BaseModel." + new_bm.id, storage.all().keys())
        self.assertIn(new_bm, storage.all().values())

    def test_stroage_save(self):
        myfile = "file.json"
        storage.save()
        self.assertTrue(os.path.exists(myfile))
        with open(myfile, 'w') as file:
            file.write("{}")
        with open(myfile, 'r') as file:
            json_dict = file.read()
            storage.save()
            new_json_dict = file.read()
        self.assertNotEqual(json_dict, new_json_dict)

    def test_storage_reload_typeError(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
