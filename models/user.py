#!/usr/bin/python3
"""this module contains definition of class User"""

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
