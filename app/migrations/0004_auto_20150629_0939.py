# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_video_shares'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_text', models.CharField(max_length=50)),
            ],
        ),

        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dislike_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),

        migrations.RemoveField(
            model_name='video',
            name='dislikes',
        ),

        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),

        migrations.RemoveField(
            model_name='video',
            name='shares',
        ),

        migrations.RemoveField(
            model_name='video',
            name='views',
        ),

        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),

        migrations.RemoveField(
            model_name='video',
            name='category',
        ),

        migrations.AddField(
            model_name='view',
            name='video',
            field=models.ForeignKey(to='app.Video'),
        ),

        migrations.AddField(
            model_name='share',
            name='video',
            field=models.ForeignKey(to='app.Video'),
        ),

        migrations.AddField(
            model_name='like',
            name='video',
            field=models.ForeignKey(to='app.Video'),
        ),

        migrations.AddField(
            model_name='dislike',
            name='video',
            field=models.ForeignKey(to='app.Video'),
        ),
        
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ManyToManyField(to='app.Category'),
        ),
    ]
