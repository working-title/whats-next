# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0011_auto_20150814_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='careers',
            field=models.ManyToManyField(to='pathways.Career'),
        ),
    ]
