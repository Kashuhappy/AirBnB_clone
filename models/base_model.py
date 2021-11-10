#!usr/bin/python3
# This class BaseModel
# Defines all common attributes and methods of other classes

from uuid import uuid4
from datetime import datetime


class BaseModel:
    # Creating class BaseModel
    id = {""}

    def __str__(self, name, id, __dict__):
        self.name = name
        self.id = id
        self.__dict__ = __dict__

    def save(self):
        updated_at.append(self)

    def to_dict(self, **kwags):
        for key, value in kwags.items():
            print(key)
            print(value)
