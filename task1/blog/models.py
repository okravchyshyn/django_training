from django.db import models

# Create your models here.
class Blogs(models.Model):
    blog_tag = models.AutoField(primary_key=True)
    blog_desc = models.CharField(max_length=20)
    blog_text = models.CharField(max_length=200)
    blog_date = models.DateTimeField('date published')


