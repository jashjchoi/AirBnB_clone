#!/usr/bin/python3
"""
    Defines a class base_model
"""
import uuid
import models
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ Initialize a new model
        """
        if kwargs:
            for key, val in kwargs['kwargs'].items():
<<<<<<< HEAD
                # if key == "created_at" or key == "updated_at":
                #    import pdb; pdb.set_trace()
                #    time_val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                #    setattr(self, key, time_val)
                if key != "__class__":
                    setattr(self, key , val)
=======
                if key != "__class__":
                    setattr(self, key, val)
>>>>>>> 553f31354e0b2f16656c48ca48d1322a1598df32

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Return a string to print id, name, and dict """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attr update_at to current time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dict contains keys/value of dict of the inst
        """
        update_dict = self.__dict__
        update_dict.update({"__class__": self.__class__.__name__})
        update_dict.update({"created_at": self.created_at.isoformat()})
        update_dict.update({"updated_at": self.updated_at.isoformat()})

        return update_dict
