#!/usr/bin/python3
"""
Review module
Inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(Basemodel):
    """
    Public class attributes;
        place_id: empty string, will be Place.id
        user_id: empty string, will be User.id
        text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
