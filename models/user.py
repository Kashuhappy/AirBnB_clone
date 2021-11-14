#!/usr/bin/python3
"""
Inherits from BaseModel
Represents a user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
