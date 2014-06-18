from django.db import models

# Create your models here.
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy, sqlalchemy.orm
import datetime

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    email = Column(String(50)) 
    pass_hash = Column(String(200))
    twit_hash = Column(String(200))
    flag_new = Columnt(Boolean)

class Words(Base):
   __tablename__ = 'words'
   id = Column( Integer, ForeignKey(Users.id))
   words = Column(String(20))
    
