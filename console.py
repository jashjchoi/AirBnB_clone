#!/usr/bin/python3
"""
    AirBnB console.py
"""
import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel


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
            my_cls = {"BaseModel": BaseModel}
            if line in my_cls.keys():
                new_model = my_cls[line]()
                new_model.save()
                print(new_model.id)
            else: 
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
