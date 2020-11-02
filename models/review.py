#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """ class review calls placeid & userid with text"""
    place_id = ""
    user_id = ""
    text = ""
