# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0005_qualification_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='debt',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
