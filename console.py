#!/usr/bin/python3
"""this module defines HBNBCommand class, which
will run our console, which will help us to perform
create, update, show, destory differnt obects"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_name = ["BaseModel", "User", "State", "City", "Place",
                  "Amenity", "Review"]
    class_ = [BaseModel, User, State, City, Place, Amenity, Review]

    def do_create(self, line):
        """ create a new object of the following classes
        BaseModel, User, State, City, Amenity, Place, Review
        if create is only specified or class name which doesn't
        belong in the above list is specified, it will show Error
        message"""
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        else:
            for i in range(len(HBNBCommand.class_name)):
                if line[0] == HBNBCommand.class_name[i]:
                    obj1 = HBNBCommand.class_[i]()
                    storage.save()
                    print(obj1.id)

    def do_show(self, line):
        """ Prints the string representation of an instance based
        on the class name and id, both class name and id have to
        be specified, otherwise it will show error message"""
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            if (line[0] + "." + line[1]) not in all_obj.keys():
                print("** no instance found **")
            else:
                print(all_obj[line[0] + "." + line[1]])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id.
        if both class and id are given and if both are correct,
        the instance with the given class name and ID will be
        deleted"""
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            if (line[0] + "." + line[1]) not in all_obj.keys():
                print("** no instance found **")
            else:
                del all_obj[line[0] + "." + line[1]]
                storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name. if all alone is specified
        it will list all objects. if class name is specifed along
        with all, all list which belong to the specified class will
        be listed"""
        line = line.split(" ")
        all_obj = storage.all()
        list1 = []
        if line[0] == "":
            for keys, values in all_obj.items():
                list1.append(str(values))
            print(list1)
        elif line[0] in HBNBCommand.class_name:
            for keys, values in all_obj.items():
                tmp = keys.split(".")
                if tmp[0] == line[0]:
                    list1.append(str(values))
            print(list1)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            all_obj = storage.all()
            if (line[0] + "." + line[1]) not in all_obj.keys():
                print("** no instance found **")
            elif len(line) < 3:
                print("** attribute name missing **")
            elif len(line) < 4:
                print("** value missing **")
            else:
                obj = all_obj[line[0] + "." + line[1]]
                if line[3].startswith('"') or line[3].startswith("'"):
                    if line[3].endswith('"') or line[3].endswith("'"):
                        line[3] = line[3].replace('"', '').replace("'", "")
                        setattr(obj, line[2], line[3])
                    else:
                        str1 = line[3] + " " + line[4]
                        str1 = str1.replace('"', '').replace("'", "")
                        setattr(obj, line[2], str1)
                elif "." in line[3]:
                    try:
                        setattr(obj, line[2], float(line[3]))
                    except (TypeError, ValueError):
                        setattr(obj, line[2], line[3])
                else:
                    try:
                        setattr(obj, line[2], int(line[3]))
                    except (TypeError, ValueError):
                        setattr(obj, line[2], line[3])
                storage.save()

    def do_count(self, line):
        """counts the number of previously created instances of
        a specified class, if the specified class does not belong
        to the defined classes or the class was not sepecified error
        message will be shown"""
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in HBNBCommand.class_name:
            print("** class doesn't exist **")
        elif line[0] in HBNBCommand.class_name:
            all_obj = storage.all()
            count = 0
            for keys, values in all_obj.items():
                tmp = keys.split(".")
                if tmp[0] == line[0]:
                    count = count + 1
            print(count)

    def update_dict(self, command, line):
        attr = line.split("{")[1][0:-2].replace(":", "").split(", ")
        for item in attr:
            comm = command + " " + item
            self.onecmd(comm)

    def default(self, line):
        if "." in line:
            line = line.replace('.', ' ').replace('(', ' ').replace(')', ' ')
            line = line.replace(',', ' ').replace('"', '').replace("'", "")
            line = line.strip().split(" ")
            line[0], line[1] = line[1], line[0]
            methods = ["all", "count", "show", "destroy", "update"]
            if line[0] in methods and line[1] in HBNBCommand.class_name:
                self.onecmd(" ".join(line))
                return None
        return cmd.Cmd.default(self, line)

    def do_quit(self, line):
        """ quit will terminate the console"""
        return True

    def do_EOF(self, line):
        """ pressing ctlr+d will exit the console"""
        return True

    def emptyline(self):
        """
        Ignore blank lines (ENTER)
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
