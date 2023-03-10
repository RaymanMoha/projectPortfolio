#!/usr/bin/python3
from sqlalchemy.orm import relationship, sessionmaker

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, create_engine, engine


class User(BaseModel, Base):
    """Representation of a user instance"""

    __tablename__: str = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    user_event = relationship("UserEvent", backref="user",
                               cascade="delete")
