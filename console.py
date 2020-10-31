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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
