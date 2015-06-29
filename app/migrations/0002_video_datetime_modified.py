# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='datetime_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 27, 3, 32, 55, 98556, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
