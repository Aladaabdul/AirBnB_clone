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
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_instance = globals()[class_name](**value)
                key = "{}.{}".format(class_name, obj_instance.id)
                FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
