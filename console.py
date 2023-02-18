#!/usr/bin/env python3
"""
Entry point of the command interpreter
"""

import cmd
import shlex
import models
from models.base_model import BaseModel
from models import storage


def do_quit(arg):
    """
    Exit the program
    """
    return True


class GHCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = '(ghke) '

    def do_quit(self, arg):
        """
        Exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        return True

    def emptyline(self):
        """
        Does nothing on empty line
        """
        pass

        def do_create(self, line):
            """Create a new instance of BaseModel, saves it to the JSON file
            and prints the id"""
            args = shlex.split(line)
            if len(args) == 0:
                print("** class name missing **")
                return
            if args[0] not in self.valid_models:
                print("** class doesn't exist **")
                return
            instance = models.storage.create(args[0])
            models.storage.save()
            print(instance.id)

        def do_show(self, line):
            """Prints the string representation of an instance based on the class
            name and id"""
            args = shlex.split(line)
            if len(args) == 0:
                print("** class name missing **")
                return
            if args[0] not in self.valid_models:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
                return
            print(models.storage.all()[key])

        def do_destroy(self, line):
            """Deletes an instance based on the class name and id"""
            args = shlex.split(line)
            if len(args) == 0:
                print("** class name missing **")
                return
            if args[0] not in self.valid_models:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
                return
            models.storage.delete(key)
            models.storage.save()

        def do_all(self, line):
            """Prints all string representation of all instances based or not on
            the class name"""
            args = shlex.split(line)
            objects = models.storage.all()
            if len(args) == 0:
                print([str(objects[key]) for key in objects])
                return
            if args[0] not in self.valid_models:
                print("** class doesn't exist **")
                return
            print([str(objects[key]) for key in objects if key.startswith(args[0] + '.')])

        def do_update(self, line):
            """Updates an instance based on the class name and id by adding or
            updating attribute"""
            args = shlex.split(line)
            if len(args) == 0:
                print("** class name missing **")
                return
            if args[0] not in self.valid_models:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + '.' + args


if __name__ == '__main__':
    GHCommand().cmdloop()
