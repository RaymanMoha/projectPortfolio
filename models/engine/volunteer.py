#!/usr/bin/python3
"""
    Define the class Volunteer.
"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String


class Volunteer(BaseModel):
    """
        Define the class Image that inherits from BaseModel.
    """
    __tablename__ = "volunteer"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    volunteer_name = Column(String(128), nullable=False)
    volunteer_path = Column(String(128), nullable=False)
    event = relationship("Event", backref="volunteer", cascade="delete")
    ngo = relationship("ngo", backref="volunteer, event", cascade="delete")