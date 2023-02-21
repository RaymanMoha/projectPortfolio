#!/usr/bin/python3
"""This module creates a unique FileStorage
instance for this application"""

from models.engine.file_storage import FileStorage
from models.user import User
from models.NGO import Ngo
from models.volunteer import Volunteer
from models.Event import Event
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage

classes = {"User": User, "BaseModel": BaseModel,
           "Volunteer": Volunteer, "NGO": Ngo, "Event": Event}

storage = FileStorage()
storage.reload()
