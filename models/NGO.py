#!/usr/bin/python3
"""
    Define the class Image.
"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String


class Ngo(BaseModel):
    """
        Define the class Image that inherits from BaseModel.
    """
    __tablename__ = "ngo"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    ngo_name = Column(String(128), nullable=False)
    ngo_path = Column(String(128), nullable=False)
    volunteer = relationship("Volunteer", backref="ngo", cascade="delete")
    event = relationship("Event", backref="volunteer, ngo", cascade="delete")
