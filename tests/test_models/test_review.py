#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test class Review"""

    @classmethod

    def test_setupReview(cls):
        cls.review = Review()
        cls.review.name = "David"
        cls.review.place_id = "2468-1012"
        cls.review.user_id = "12345-67890"
        cls.review.text = "I love this place!"

    def test_Review_instance(self):
        """test if the obj is an inst of Review, BaseModel
        """
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertIsInstance(obj, BaseModel)

    def test_Review_attr(self):
        review_obj = Review()
        self.assertIn("id", review_obj.__dict__)
        self.assertIn("created_at", review_obj.__dict__)
        self.assertIn("updated_at", review_obj.__dict__)
        self.assertIn("place_id", Review.__dict__)
        self.assertIn("user_id", Review.__dict__)
        self.assertIn("text", Review.__dict__)
        """test if attr in correct type"""
        self.assertEqual(type(review_obj.user_id), str)
        self.assertEqual(type(review_obj.place_id), str)
        self.assertEqual(type(review_obj.text), str)

    def test_Review_to_save(self):
        """test if the save() works"""
        tmpobj = Review()
        tmpobj.save()
        self.assertNotEqual(tmpobj.created_at, tmpobj.updated_at)


if __name__ == "__main__":
    unittest.main()
