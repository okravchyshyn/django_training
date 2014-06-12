#from django.db import models
# Create your models here.

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy, sqlalchemy.orm
import datetime


Base = declarative_base()

#engine = sqlalchemy.create_engine('mysql://user:user@localhost/blog_db')
#Session = sqlalchemy.orm.sessionmaker(bind=engine)
#session = Session()
#Base.metadata.create_all(engine)

class Blogs(Base):
    __tablename__ = 'blogs'
    blog_tag = Column(Integer, primary_key=True)
    blog_desc = Column(String(20))
    blog_text = Column(String(200))
    blog_date = Column(DateTime, onupdate=datetime.datetime.now, 
                    default=datetime.datetime.max)

    def __init__(self, desc, msg, dt):
        self.blog_desc = desc
        self.blog_text = msg
        print dt
        #self.blog_date = str(dt)

    def __repr__(self):
        return u"Language(%s, %s)" % (self.blog_desc, self.blog_text)

engine = sqlalchemy.create_engine('mysql://user:user@localhost/blog_db')
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

#class Blogs(models.Model):
#    blog_tag = models.AutoField(primary_key=True)
#    blog_desc = models.CharField(max_length=20)
#    blog_text = models.CharField(max_length=200)
#    blog_date = models.DateTimeField('date published')



def add_new_blog(desc, message):
    print "add_new_blog"
    print "desc:", desc
    print "msg:", message
    from django.utils import timezone
    b = Blogs(desc=desc
         , msg = message
         , dt = datetime.datetime.now)
    
    #b.save()
    session.add(b)
    session.commit()

def get_all_items():
    return session.query(Blogs).all()

def get_blog_items(pk_id):
    #b = Blogs.objects.get(pk=pk_id)
    b = session.query(Blogs).filter_by(blog_tag=pk_id).one() 
    print "get_blog_items=", b.blog_desc, " and ", b.blog_text 
    return (b.blog_desc, b.blog_text)

def update_blog_item(pk_id, desc, msg):
    print "update_blog_item:", desc, " ", msg
    #b = Blogs.objects.get(pk=pk_id)
    b = session.query(Blogs).filter_by(blog_tag=pk_id).one() 
   
    b.blog_desc = desc
    b.blog_text = msg
    #b.blog_date = models.DateTimeField('date published')
    print "before save"
    print b
    #b.save()
    session.commit()
    print "updated"
