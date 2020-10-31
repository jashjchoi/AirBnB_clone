#!/usr/bin/python3
"""file for storage engine"""
import json
import models


class FileStorage():
    """
    serializes instances to a JSON file & deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.update({"{}.{}".format(obj, obj.id): obj.to_dict()})

    def save(self):
        self.__file_path = "file.json"
        with open(self.__file_path, "w") as myfile:

            json.dump(self.__objects, myfile, default=str)

    def reload(self):
        try:
            with open(self.__file_path, "r") as myfile:
                return self.__objects.update(json.load(myfile))

        except FileNotFoundError:
            pass
