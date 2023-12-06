#!/usr/bin/python3
"""User class defination

"""
from models.base_model import BaseModel
import json

class User(BaseModel):
    """Class defination

    Atrributes:
    email(string): string
    password: empty
    first_name: empty
    last_name: string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
