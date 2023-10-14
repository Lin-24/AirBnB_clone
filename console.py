#!/usr/bin/python3
"""Console module for AirBnB Clone Project"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles end of file (EOF)"""
        return True

    def emptyline(self):
        """Do nothing on an empty line + ENTER"""
        pass

    def do_create(self, args):
        """Creates a new instance saves it (to the JSON file) and prints it"""

        args = args.split()
        if len(args) == 0:
            print("** Class name missing **")
        elif args[0] in HBNBCommand.__classes:
            new_creation = eval(args[0] + '()')
            models.storage.save()
            print(new_creation.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an
            instance based on the class name and id"""

        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
        if key_value in obj:
            print(obj[key_value])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
            and id (save the change into the JSON file)"""

        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
        if key_find in objects.keys():
            objects.pop(key_find, None)
            models.storage.save()
        else:
            print('** no instance found **')

    def do_all(self, args):
        """Prints all string representation of all
           instances based or not on the class name."""

        args = args.split()
        objects = models.storage.all()
        new_list = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by
            adding or updating attribute (save the change to JSON file)."""

        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """Checks if the user typed class name and id."""

        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Checks class id"""

        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Finds the name class."""

        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
