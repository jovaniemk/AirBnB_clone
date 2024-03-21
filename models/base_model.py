#!/usr/bin/python3
"""this module will contain base_model class"""

from uuid import uuid4
from datetime import datetime
class BaseModel:
   """BaseModel class"""
   def __init__(self, *args, **kwargs):
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
   def __str__(self):
      """string representation of an object"""
      return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
   def save(self):
      """updates updated_at attribute"""
      self.updated_at = datetime.now(tz=None)
   def to_dict(self):
      tmp = self.__dict__.copy()
      tmp['__class__'] = self.__class__.__name__
      tmp['created_at'] = self.created_at.isoformat()
      tmp['updated_at'] = self.updated_at.isoformat()
      return tmp
