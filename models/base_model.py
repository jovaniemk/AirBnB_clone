#!/usr/bin/python3
"""this module will contain BaseModel class
BaseModel class will be a blue print for other
classes which will be defined using attributes of
BaseModel"""


from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class, this class will define common attributes
    for all the classes which will be later defined
    Attributes:
    id(str): unique id for each object
    created_at(datetime.datetime): time in wich the object is created
    updated_at(datetime.datetime): time in which the object is updated
    """

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
        """this instance method will return string representation of an object
        this string representation will contain class_name,
        id of the object and dict attribute of the object"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """this method will save the new attributes of the object to
        the File_Storage class and will change to the updated_at attribute
        to the new time"""
        self.updated_at = datetime.now(tz=None)
        storage.save()

    def to_dict(self):
        """this instance method will return a dictionary representation
        of an object, this method will copy the dict attribute of the
        object with some modifications.it will change cretaed_at and
        updated_at attribute to iso_format and add __class__ key to
        the dictionary"""
        tmp = self.__dict__.copy()
        tmp['__class__'] = self.__class__.__name__
        tmp['created_at'] = self.created_at.isoformat()
        tmp['updated_at'] = self.updated_at.isoformat()
        return tmp
