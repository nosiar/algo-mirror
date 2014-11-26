# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='problem',
            name='keyword',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(unique=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(unique=True),
        ),
    ]
