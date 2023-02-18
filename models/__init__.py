#!/usr/bin/python3
"""This module creates a unique FileStorage
instance for this application"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()