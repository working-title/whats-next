# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0003_career_interest_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='maori_name',
            field=models.CharField(max_length=256, blank=True),
        ),
    ]
