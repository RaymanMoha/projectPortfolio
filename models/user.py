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


Event = relationship("Event", backref="User", cascade="delete")


# engine = create_engine(f'mysql://{guidehub_dev}:{guidehub_dev_pwd}@{localhost}/{guidehub_dev_db}')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session
