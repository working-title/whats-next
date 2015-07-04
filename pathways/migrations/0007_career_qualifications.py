# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0006_auto_20150704_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='qualifications',
            field=models.ManyToManyField(to='pathways.Qualification'),
        ),
    ]
