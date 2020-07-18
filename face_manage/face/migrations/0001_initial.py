# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('uphone', models.CharField(max_length=11)),
                ('face_image', models.CharField(max_length=50)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='visitor_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vname', models.CharField(max_length=10)),
                ('vtemp', models.FloatField()),
                ('vtime', models.DateTimeField()),
                ('vuser', models.ForeignKey(to='face.user_info')),
            ],
        ),
    ]
