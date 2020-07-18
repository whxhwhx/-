# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0002_remove_user_info_face_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor_info',
            name='vname',
        ),
    ]
