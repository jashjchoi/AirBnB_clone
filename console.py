#!/usr/bin/python3
"""
    AirBnB console.py
"""
import json
import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Ignores empty input and execute nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at EOF"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to JSON"""
        if not line:
            print("** class name missing **")
        else:
            my_cls = {"BaseModel": BaseModel, "User": User,
                      "State": State, "City": City,
                      "Amenity": Amenity, "Place": Place,
                      "Review": Review}
            if line in my_cls.keys():
                new_model = my_cls[line]()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        """
        try:
            if not line:
                raise SyntaxError()
            x = line.split()
            my_cls = {"BaseModel": BaseModel, "User": User,
                      "State": State, "City": City,
                      "Amenity": Amenity, "Place": Place,
                      "Review": Review}
            if x[0] not in my_cls:
                raise NameError()
            if len(x) < 2:
                raise IndexError()
            jsondict = storage.all()
            key = x[0] + '.' + x[1]
            if key not in jsondict:
                raise KeyError()
            if len(x) < 3:
                raise AttributeError()
            if len(x) < 4:
                raise ValueError()
            val = jsondict[key]
            attribute_name = x[2]
            attribute_value = x[3]
            try:
                val.__dict__[attribute_name] = eval(attribute_value)
            except Exception:
                val.__dict__[attribute_name] = attribute_value
            val.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def do_destroy(self, line):
        my_cls = {"BaseModel": BaseModel, "User": User,
                  "State": State, "City": City,
                  "Amenity": Amenity, "Place": Place,
                  "Review": Review}
        try:
            if not line:
                raise SyntaxError()
            x = line.split(" ")
            if x[0] not in my_cls:
                raise NameError()
            if len(x) < 2:
                raise IndexError()
            jsondict = storage.all()
            key = x[0] + '.' + x[1]
            if key in jsondict.keys():
                del jsondict[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_show(self, line):
        try:
            if not line:
                raise SyntaxError()
            """x = input"""
            x = line.split()
            my_cls = {"BaseModel": BaseModel, "User": User,
                      "State": State, "City": City,
                      "Amenity": Amenity, "Place": Place,
                      "Review": Review}
            if x[0] not in my_cls:
                raise NameError()
            if len(x) < 2:
                raise IndexError()
            key = x[0] + "." + x[1]
            jsondict = storage.all()
            if key in jsondict.keys():
                print(jsondict[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        jsondict = storage.all()
        try:
            if line:
                my_cls = {"BaseModel": BaseModel, "User": User,
                          "State": State, "City": City,
                          "Amenity": Amenity, "Place": Place,
                          "Review": Review}
                if line not in my_cls:
                    raise NameError()
            for key in jsondict.keys():
                if line:
                    x = key.split(".")
                    if x[0] == line:
                        print(jsondict[key])
                else:
                    print(jsondict[key])
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
