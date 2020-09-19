# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('roomID', models.IntegerField()),
                ('loc', models.CharField(max_length=20)),
                ('roomName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=5)),
                ('course', models.CharField(max_length=20)),
                ('room', models.OneToOneField(to='session_app.ClassRoom', default='')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='room',
            field=models.ForeignKey(default='', to='session_app.ClassRoom'),
        ),
    ]
