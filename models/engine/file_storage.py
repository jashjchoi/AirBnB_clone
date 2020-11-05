#!/usr/bin/python3
"""file for storage engine"""
import json
import datetime


class FileStorage():
    """
    serializes instances to a JSON file & deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file"""
        self.__file_path = "file.json"
        with open(self.__file_path, "w") as myfile:
            json.dump(self.__objects, myfile, default=str)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as myfile:
                file_dict = json.load(myfile)
                for key in file_dict:
                    clsid = key.split(".")
                    class_id_str = "[{}] ({}) ".format(clsid[0], clsid[1])
                    attr_dict = eval(file_dict[key].replace(class_id_str, ""))
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.place import Place
                    from models.review import Review
                    my_cls = {'BaseModel': BaseModel, 'User': User,
                              "State": State, "City": City,
                              "Amenity": Amenity, "Place": Place,
                              "Review": Review}
                    if clsid[0] in my_cls.keys():
                        new_model = my_cls[clsid[0]](kwargs=attr_dict)
                        self.__objects.update({key: new_model})
                return self.__objects

        except FileNotFoundError:
            pass
