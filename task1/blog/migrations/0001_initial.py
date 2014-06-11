# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('blog_tag', models.AutoField(serialize=False, primary_key=True)),
                ('blog_desc', models.CharField(max_length=20)),
                ('blog_text', models.CharField(max_length=200)),
                ('blog_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
