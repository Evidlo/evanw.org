# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141012_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=projects.models.folder_location)),
                ('description', models.CharField(max_length=200, verbose_name=b'image description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'project title')),
                ('text', models.TextField(verbose_name=b'project text')),
                ('thumbnail', sorl.thumbnail.fields.ImageField(upload_to=b'projects')),
                ('categories', models.ManyToManyField(to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
    ]
