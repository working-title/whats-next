# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0012_industry_careers'),
    ]

    operations = [
        migrations.AddField(
            model_name='industry',
            name='description',
            field=models.TextField(default="Default Industry Description (Fill me in!)"),
            preserve_default=False,
        ),
    ]
