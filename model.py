from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Storis(Base):
    __tablename__  = 'storis'
    id             = Column(Integer, primary_key=True)  
    name           = Column(String)
    author         = Column(String)
    tags           = Column(String)
    rating         = Column(Integer)
    description    = Column(String)
    text           = Column(String)
    pic_url        = Column(String)

class Users(Base):
    __tablename__  = 'users'
    id             = Column(Integer, primary_key=True)
    username       = Column(String)
    password       = Column(String)