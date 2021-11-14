#!/usr/bin/python3
""" Create a unique FileStorage instance for your application"""

from models.engine import file_storage

storage = file_storage.Filestorage()
storage.reload()
