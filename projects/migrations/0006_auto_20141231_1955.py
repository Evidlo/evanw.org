# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateField(default=datetime.date(2014, 12, 31), verbose_name=b'publish date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default='Complete', max_length=16, verbose_name=b'status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=200, verbose_name=b'image description', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name=b'short description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='text',
            field=models.TextField(verbose_name=b'description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'title'),
        ),
    ]
