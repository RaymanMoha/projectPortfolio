#!/usr/bin/python3
"""
    Implementing the console for the I-Share Project
"""

import re
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.user_event import UserEvent
from models.Event import Event
from sqlalchemy.orm import sessionmaker, scoped_session


class GHCommand(cmd.Cmd):
    """
        Contains the entry point of the command interpreter.
    """

    prompt = ("(i-share) ")

    def do_quit(self, args):
        """
            Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
            Exits after receiving the EOF signal.
        """
        return True

    def do_create(self, args):
        """
            Create a new instance of class BaseModel and saves it
            to the JSON file.
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = re.split(r"\s|=", args)
            new_instance = eval(args[0])()

            for idx in range(1, len(args), 2):
                key = args[idx]
                value = args[idx + 1]
                try:
                    new_instance.__getattribute__(key)
                except AttributeError:
                    continue
                if re.search("^\".*\"$|^\'.*\'$", value) is not None:
                    value = value.replace("_", " ")
                    value = value.replace("\"", "")
                    value = value.replace("\'", "")
                elif re.search('[+-]?[0-9]+\.[0-9]+', value) is not None:
                    value = float(value)
                elif re.search(r"\d.*", value) is not None:
                    value = int(value)
                else:
                    continue
                setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        """
            Print the string representation of an instance baed on
            the class name and id given as args.
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = models.storage
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
            Deletes an instance based on the class name and id.
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]

        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        storage = models.storage
        storage.reload()
        obj_dict = storage.all(class_name)
        key = class_name + "." + class_id
        delete__obj = obj_dict[key]
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.delete(delete__obj)

    def do_all(self, args):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        obj_list = []
        storage = models.storage
        storage.reload()
        try:
            if len(args) != 0:
                eval(args)
            if len(args) == 0:
                objects = storage.all()
            else:
                objects = storage.all(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)

        print(obj_list)

    def do_update(self, args):
        """
            Update an instance based on the class name and id
            sent as args.
        """
        storage = models.storage
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

    def emptyline(self):
        """
            Prevents printing anything when an empty line is passed.
        """
        pass

    def do_count(self, args):
        """
            Counts/retrieves the number of instances.
        """
        obj_list = []
        storage = models.storage
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))

    def default(self, args):
        """
            Catches all the function names that are not expicitly defined.
        """
        functions = {"all": self.do_all, "update": self.do_update,
                     "show": self.do_show, "count": self.do_count,
                     "destroy": self.do_destroy, "update": self.do_update}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))

        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except Exception as ex:
            print("*** Unknown syntax:", args[0])


if __name__ == "__main__":
    """
        Entry point for the loop.
    """
    GHCommand().cmdloop()
