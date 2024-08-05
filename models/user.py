#!/usr/bin/python3
"""User Model"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """Representation of a User"""
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initialize a new User"""
        super().__init__(*args, **kwargs)
        if 'email' in kwargs:
            self.email = kwargs['email']
        if 'password' in kwargs:
            self.password = kwargs['password']
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']
