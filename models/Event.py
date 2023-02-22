#!/usr/bin/python3
"""
    Define the class Image.
"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Table


user_event = Table('user_event', Base.metadata,
                      Column('user_id', String(60),
                             ForeignKey('user.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True),
                      Column('event_id', String(60),
                             ForeignKey('event.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True))


class Event(BaseModel, Base):
    """
        Define the class Event that inherits from BaseModel.
    """
    __tablename__ = "event"
    name = Column(String(128))

    user = relationship("User",
                             secondary=user_event,
                             viewonly=False)
