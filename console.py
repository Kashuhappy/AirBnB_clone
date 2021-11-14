#!usr/bin/python3
"""
The entry point of the command interpreter
Console to the Module
"""
import cmd
from model.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place


class HBNHCommand(cmd.Cmd):
    """ AirBnB command line interpreter """
    prompt = "hbnb"
    valid_classes = {'BaseModel' = BaseModel, 'User' = User, 'City' = City
                     'Amenity' = Amenity, 'Place' = Place, 'Review' = Review}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn't execute anything"""
        pass

    def d0_create(self):
        """
        Creates and instance of BaseModel
        Save it to JSON file
        Prints id
        """
        if len(line) == 0:
            self.perror(1)
        elif line not in HBNBCommand.valid_classes.keys():
            self.perror(2)
        else:
            model = HBHBCommand.valid_classes[line]()
            model.save()
            print(model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        Based on the class name and id
        """
        data = line.split()
        if len(line) == 0:
            self.perror(1)
        elif data[0] not in HBNBCommand.valid_classes.keys():
            self.perror(2)
        elif len(data) == 1:
            self.perror(3)
        else:
            key = data[0] + "." + data[1]
            all_objs = storage.all()
            if key not in all all_objs.keys():
                self.perror(4)
            else:
                print(all_objs[keys])

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        data = line.split()
        if len(line) == 0:
            self.perror(1)
        elif data[0] not in HBNBCommand.valid_classes.keys():
            self.perror(2)
        elif len(data) == 1:
            self.perror(3)
        else:
            key = data[0] + "." + data[1]
            all_objs = storage.all()
            if key not in all_objs.keys():
                self.perror(4)
            else:
                del (all_objs([key])
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        Based or not on the class name
        """
        all_instances = storage.all()
        if len(line) == 0:
            all_objs = []
            for k, obj in all_instances.items():
                all_objs.append(str(obj))
            print(all_objs)
        elif line in HBNBCommand.valid_classes.keys():
            objs = []
            for key, value in all_instances.items():
                if line == value.__class__.__name__:
                    key = line + "." + str(value.id)
                    objs.append(str(all_instances[key]))
            print(objs)
        else:
            self.perror(2)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        And id by adding or updating attribute
        """
        data = line.spli()
        if len(line) == 0:
            self.perror(1)
        elif data[0] not in HBHBCommand.valid_classes.keys():
            self.perror(2)
        elif len(data) == 1:
            self.perror(3)
        elif len(data) == 2:
            self.perror (5)
        elif len(data) == 3:
            self.perror (6)
        else:
            obj = all_storage[key]
            setattr(obj, data[2], data[3])
            storage.save()

    def perror(self, code):
        """
        Function for printing common errors
        """
        if code == 1:
            print("** class name missing **")
        if code == 2:
            print("** class doesn't exist **")
        if code == 3:
            print("** instance id missing **")
        if code == 4:
            print("** no instance found **")
        if code == 5:
            print("** attribute name missing **")
        if code == 6:
            print("** value missing **")

if __name__ == '__main__':
    HBNHCommand().cmdloop()
