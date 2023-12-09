#!/usr/bin/python3
"""Base class defination of all other classes

"""

import uuid
from datetime import datetime, timedelta
import models


class BaseModel:
    """Class defination


    """

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class

        Args:
        id(string): id
        created_at(datetime): datetime
        updated_at(datetime): datetime

        Return: None
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime
                                .strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str Function

        Args:
        None

        Return: class name, id, __dict__
        """
        return f"[{self.__class__.__name__}] {(self.id)} {self.__dict__}"

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def save(self):
        """
        save function
        
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict function

        """

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
