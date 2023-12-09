#!/usr/bin/python3
"""Class File storage defination


"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Class declaration

    Attributes:
    __file_path(string): path to the JSON file
    __objects(dictionary): store all objects
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def all(self):
        """all function declaration

        Args:
        None

        Return: dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """new function declaration

        Args:
        obj: Key

        Returns: None
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save function declaration

        Args:
        None

        Returns: None
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """reload function declaration

        Args:
        None

        Returns: None
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name) (**o))
        except FileNotFoundError:
            return
