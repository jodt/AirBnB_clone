#!/usr/bin/python3
"""
This module serializes instances to a JSON file
and deserializes JSON file to instances
"""

from os.path import exists
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
import json


class FileStorage:
    """
    This class creates a FileStorage Instance
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This function returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        This function sets in __objects the obj with
        key <obj class name>.id
        """
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """
        This function serializes __objects to
        the JSON file (path: __file_path)
        """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(dict, file, indent=2)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file

        Return:
            None
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fd:
                dict_json = json.load(fd)
                for key, value in dict_json.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except Exception:
            pass
