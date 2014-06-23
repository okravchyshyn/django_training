#from django.db import models

# Create your models here.
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Boolean
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
    flag_new = Column(Boolean)

class Words(Base):
   __tablename__ = 'words'
   id = Column( Integer, ForeignKey(Users.id),primary_key=True)
   words = Column(String(20), primary_key=True)
   result = Column( Integer) 
   flag_new = Column(Boolean)

    
engine = sqlalchemy.create_engine('mysql://user:user@localhost/tw_study')
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

