# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('problem', models.ManyToManyField(to='problems.Problem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
