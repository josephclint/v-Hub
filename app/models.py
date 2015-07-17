from django.db import models

from django.contrib.auth.models import User


class Tag(models.Model):
    tag_text = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tag_text


class Category(models.Model):
    category_text = models.CharField(max_length=50)

    def __unicode__(self):
        return self.category_text

    class Meta:
        verbose_name_plural = 'categories'


class Video(models.Model):
    owner = models.ForeignKey(User)
    video = models.FileField(upload_to='videos/%Y/%m/%d')
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    comment_text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    time = models.DecimalField(decimal_places=10, max_digits=10)
    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.comment_text


class Like(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    like_date = models.DateTimeField(auto_now_add=True)


class Dislike(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    dislike_date = models.DateTimeField(auto_now_add=True)


class Share(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    share_date = models.DateTimeField(auto_now_add=True)


class View(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(Video)
    view_date = models.DateTimeField(auto_now_add=True)
