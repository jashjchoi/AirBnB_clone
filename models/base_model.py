#!/usr/bin/python3
"""
    Defines a class base_model
"""
import uuid
import models
from datetime import datetime

class BaseModel:
    def __init__(self):
        """Initialize a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Return a string to print id, name, and dict
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attr update_at to current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        update_dict = self.__dict__
        update_dict.update({"__class__": self.__class__.__name__})
        update_dict.update({"created_at": self.created_at.isoformat()})
        update_dict.update({"updated_at": self.updated_at.isoformat()})
        
        return update_dict
