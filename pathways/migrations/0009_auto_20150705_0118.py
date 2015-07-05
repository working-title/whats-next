# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='degree',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='no_qualification',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='post_school',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career',
            name='school',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
