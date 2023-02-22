#!/usr/bin/python3
"""
    Define the class SharedWith.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String


class UserEvent(BaseModel, Base):
    """
        Define the class SharedWith that inherits from BaseModel.
    """
    __tablename__ = "user_event"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    event_id = Column(String(60), ForeignKey('event.id'), nullable=False)