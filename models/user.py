#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """ Define class User attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
