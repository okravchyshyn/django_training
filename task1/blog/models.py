from django.db import models

# Create your models here.
class Blogs(models.Model):
    blog_tag = models.AutoField(primary_key=True)
    blog_desc = models.CharField(max_length=20)
    blog_text = models.CharField(max_length=200)
    blog_date = models.DateTimeField('date published')



def add_new_blog(desc, msg):
    print "add_new_blog"
    print "desc:", desc
    print "msg:", msg
    from django.utils import timezone
    b = Blogs(blog_desc=desc
         , blog_text = msg
         , blog_date = timezone.now())
    b.save()

def get_blog_items(pk_id):
    b = Blogs.objects.get(pk=pk_id)
    print "get_blog_items=", b.blog_desc, " and ", b.blog_text 
    return (b.blog_desc, b.blog_text)

def update_blog_item(pk_id, desc, msg):
    print "update_blog_item:", desc, " ", msg
    b = Blogs.objects.get(pk=pk_id)
   
    b.blog_desc = desc
    b.blog_text = msg
    #b.blog_date = models.DateTimeField('date published')
    print "before save"
    print b
    b.save()
    print "updated"
