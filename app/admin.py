from django.contrib import admin

from models import Video, Tag, Comment

class VideoAdmin(admin.ModelAdmin):
	search_fields = ('title', 'description')
	fieldsets = [
		(None, {'fields': ['title', 'description', 'video']}),
		('Additional Information', {'fields': ['category', 'genre']}),
		('Statistics', {'fields': ['views', 'likes', 'dislikes']}),
	]

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)