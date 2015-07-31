# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

INITIAL_CATEGORIES = (
    ('Animation & Film', 'icons/movie.png'),
    ('Music', 'icons/music.png'),
    ('News & Politics', 'icons/news.png'),
    ('People & Blogs', 'icons/people.png'),
    ('Science & Technology', 'icons/science.png'),
    ('Sports', 'icons/sports.png'),
)


def populate_categories(apps, schema_editor):
    Category = apps.get_model("app", "Category")
    for category in INITIAL_CATEGORIES:
        Category.objects.create(category_text=category[0], icon=category[1])


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_text', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('time', models.DecimalField(max_digits=10, decimal_places=10)),
                ('datetime_added', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='app.Category')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='app.Tag', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(to='app.Video')),
            ],
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
            model_name='comment',
            name='video',
            field=models.ForeignKey(to='app.Video'),
        ),
        migrations.RunPython(populate_categories),
    ]
