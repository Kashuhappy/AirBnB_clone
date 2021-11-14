#!usr/bin/python3
"""
The entry point of the command interpreter
Console to the Module
"""
import cmd
from model.base_model import BaseModel
from models import storage

class HBNHCommand(cmd.Cmd):
    """ AirBnB command line interpreter"""
    prompt = "hbnb"
    valid_classes = {'BaseModel' = BaseModel, 'User' = User, 'City' = City, 'Am                      enity' = Amenity, 'Place' = Place, 'Review' = Review}

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

if __name__ == '__main__':
    HBNHCommand().cmdloop()
