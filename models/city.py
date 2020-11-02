#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """class city stores state id and city name"""
    state_id = ""
    name = ""
