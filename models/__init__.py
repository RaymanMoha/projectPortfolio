#!/usr/bin/python3
"""This module creates a unique FileStorage
instance for this application"""

from models.engine.file_storage import FileStorage
from models.user import User
from models.Event import Event
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage

classes = {"User": User, "BaseModel": BaseModel, "Event": Event}

storage = DBStorage()
storage.reload()
