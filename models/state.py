#!/usr/bin/python3
""" file for model state that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """ class state adds name of "state" """
    name = ""
