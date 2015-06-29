# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.FileField(upload_to=b'videos/%Y/%m/%d')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('datetime_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=2, choices=[(b'FA', b'Film & Animation'), (b'M', b'Music'), (b'PB', b'People & Blogs'), (b'NP', b'News & Politics'), (b'ST', b'Science & Technology'), (b'S', b'Sports')])),
                ('genre', models.CharField(max_length=2, choices=[(b'Co', b'Comedy'), (b'Ac', b'Action'), (b'Ad', b'Adventure'), (b'Dr', b'Drama'), (b'Ro', b'Romance')])),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='app.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(to='app.Video'),
        ),
    ]
