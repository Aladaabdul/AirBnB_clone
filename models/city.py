#!/usr/bin/python3
"""City class defination

"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class defination

    Attributes:
    state_id(String): State.id
    name(string): string
    """
    state_id = ""
    name = ""
