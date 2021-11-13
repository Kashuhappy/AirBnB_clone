#!usr/bin/python3

import json
from model.base_model import BaseModel

class FileStorage:
    """
    Private class attributes:
        __file_path
        __objects
    Public instance methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    
    __file._path = str("")
    __objects = dict()
    
    def all(self):
        """  Returns the dictionary __objects """
        return FileStorage.__objects
        
    def new(self, obj):
        """  Sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            FileStorage.__objects[key] = obj
    
    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        
        """ Opens a file, serializes, and writes in the file"""
        with open(FileStorage.__file.path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """

        try:
            with open(FileStorage.__file__path, "r",) as f:
                dict_objs = json.load(f)
            for obj in dict_objs.values():
                class_name = obj["__class__"]
                self.new(eval(class_name)(**obj))
        
        except FileNotFoundError:
            pass