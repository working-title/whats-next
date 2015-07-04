# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pathways', '0002_auto_20150704_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('income', models.PositiveIntegerField()),
                ('maori_name', models.CharField(max_length=256, blank=True)),
                ('hours_worked_30_less', models.PositiveIntegerField()),
                ('hours_worked_60_less', models.PositiveIntegerField()),
                ('hours_worked_60_more', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('maori_name', models.CharField(max_length=256)),
                ('careers', models.ManyToManyField(to='pathways.Career')),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
    ]
