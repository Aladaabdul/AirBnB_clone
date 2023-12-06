#!/usr/bin/python3
"""Review class defination

"""
from models.base_model import BaseModel


class  Review(BaseModel):
    """Review class

    Attributes:
    place_id: string
    user_id: string
    text: string
    """
    place_id = ""
    user_id = ""
    text = ""
