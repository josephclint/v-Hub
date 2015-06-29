# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_video_datetime_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='shares',
            field=models.IntegerField(default=0),
        ),
    ]
