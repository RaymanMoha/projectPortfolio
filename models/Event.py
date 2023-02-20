#!/usr/bin/python3
"""
    Define the class Image.
"""
from models.base_model import BaseModel
# from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String


class Event(BaseModel):
    """
        Define the class Event that inherits from BaseModel.
    """
    __tablename__ = "event"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    event_id = Column(String(60), ForeignKey('event.id'), nullable=False)
