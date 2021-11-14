#!/usr/bin/python3
"""
City module
Inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes:
        state_id: empty string
        name: empty string
    """
    name = ""
    state_id = ""
