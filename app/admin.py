from django.contrib import admin

from models import Video, Tag, Comment, Category, View, Like, Dislike, Share

class ViewInline(admin.TabularInline):
	model = View
	extra = 0

class LikeInline(admin.TabularInline):
	model = Like
	extra = 0

class DislikeInline(admin.TabularInline):
	model = Dislike
	extra = 0

class ShareInline(admin.TabularInline):
	model = Share
	extra = 0

class TagInline(admin.TabularInline):
	model = Video.tags.through
	verbose_name_plural = "Tags"

class CategoryInline(admin.TabularInline):
	model = Video.categories.through
	verbose_name_plural = "Categories"

class VideoAdmin(admin.ModelAdmin):
	search_fields = ('title', 'description')
	fieldsets = [
		(None, {'fields': ['title', 'description', 'video', 'owner']}),
	]
	inlines = [CategoryInline, TagInline, ViewInline, LikeInline, DislikeInline, ShareInline]

admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
admin.site.register(Category)