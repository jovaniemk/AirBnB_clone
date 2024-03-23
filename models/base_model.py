#!/usr/bin/python3
"""this module will contain BaseModel class"""


from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class, this class will define common attributes
    for all the classes which will be later defined
    Args:
    our class will eiter have no argument or dictionary representation of 
    a previously created object"""

    def __init__(self, *args, **kwargs):
        """this method will intialize our BaseModel object
        Args:
        args: variable size arguments
        kwargs: variabe size keyword arguments
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            tmp = datetime.now(tz=None)
            self.created_at = tmp
            self.updated_at = tmp
            storage.new(self)

    def __str__(self):
        """this instance method will return string representation of an object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates updated_at attribute"""
        self.updated_at = datetime.now(tz=None)
        storage.save()

    def to_dict(self):
        """this instance method will return a dictionary representation of an object"""
        tmp = self.__dict__.copy()
        tmp['__class__'] = self.__class__.__name__
        tmp['created_at'] = self.created_at.isoformat()
        tmp['updated_at'] = self.updated_at.isoformat()
        return tmp
