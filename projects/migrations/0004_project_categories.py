# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141012_2129'),
        ('projects', '0003_remove_project_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(to='blog.Category'),
            preserve_default=True,
        ),
    ]
