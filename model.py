from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Storis(Base):
    __tablename__  = 'storis'
    id             = Column(Integer, primary_key=True)
    author         = Column(String)
    rating         = Column(Integer)
    description    = Column(String)
    pic_url        = Column(String)

class Users(Base):
    id             = Column(Integer, primary_key=True)
    username       = Column(String)
    password       = Column(String)