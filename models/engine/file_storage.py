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
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def save(self):
        self.__file_path = "file.json"
        with open(self.__file_path, "w") as myfile:
            json.dump(self.__objects, myfile, default=str)

    def reload(self):
        try:
            with open(self.__file_path, "r") as myfile:
                file_dict = json.load(myfile)
                for key in file_dict:
<<<<<<< HEAD
                    class_id = key.split(".")
                    class_id_str = "[{}] ({}) ".format(class_id[0], class_id[1])
                    attr_dict = eval(file_dict[key].replace(class_id_str, ""))
                    from models.base_model import BaseModel
                    my_cls = {'BaseModel': BaseModel}
                    if class_id[0] in my_cls.keys():
                        new_model = my_cls[class_id[0]](kwargs=attr_dict)
                        self.__objects.update({key: new_model})
                return self.__objects

=======
                    clsid = key.split(".")
                    class_id_str = "[{}] ({}) ".format(clsid[0], clsid[1])
                    attr_dict = eval(file_dict[key].replace(class_id_str, ""))
                    from models.base_model import BaseModel
                    my_cls = {'BaseModel': BaseModel}
                    if clsid[0] in my_cls.keys():
                        new_model = my_cls[clsid[0]](kwargs=attr_dict)
                        self.__objects.update({key: new_model})
                return self.__objects
>>>>>>> 553f31354e0b2f16656c48ca48d1322a1598df32
        except FileNotFoundError:
            pass
