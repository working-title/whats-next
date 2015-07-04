# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('income', models.PositiveIntegerField()),
                ('maori_name', models.CharField(max_length=256)),
                ('hours_worked_30_less', models.PositiveIntegerField()),
                ('hours_worked_60_less', models.PositiveIntegerField()),
                ('hours_worked_60_more', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
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
