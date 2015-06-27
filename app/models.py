from django.db import models

from django.contrib.auth.models import User

CATEGORIES = (
	('FA', 'Film & Animation'),
	('M', 'Music'),
	('PB', 'People & Blogs'),
	('NP', 'News & Politics'),
	('ST', 'Science & Technology'),
	('S', 'Sports'),
)

GENRES = (
	('Co', 'Comedy'),
	('Ac', 'Action'),
	('Ad', 'Adventure'),
	('Dr', 'Drama'),
	('Ro', 'Romance'),
)

class Tag(models.Model):
	tag_text =  models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.tag_text

class Video(models.Model):
	owner = models.ForeignKey(User)
	video = models.FileField(upload_to='videos/%Y/%m/%d')
	title = models.CharField(max_length=200)
	description = models.TextField()
	datetime_added = models.DateTimeField(auto_now_add=True)
	datetime_modified = models.DateTimeField(auto_now=True)
	category = models.CharField(max_length=2, choices=CATEGORIES)
	genre = models.CharField(max_length=2, choices=GENRES)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	shares = models.IntegerField(default=0)
	tags = models.ManyToManyField(Tag)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	video = models.ForeignKey(Video)
	comment_text = models.TextField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.comment_text