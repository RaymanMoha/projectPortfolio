#!/usr/bin/python3
"""
    Define the class Image.
"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Table

class Event(BaseModel, Base):
    """
        Define the class Event that inherits from BaseModel.
    """
    __tablename__ = "event"
    name = Column(String(128))

    user_event = relationship("UserEvent", backref="event",
                               cascade="delete")
