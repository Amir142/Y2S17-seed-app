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

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel