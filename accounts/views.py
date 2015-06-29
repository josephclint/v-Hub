from django.shortcuts import render

from app.views import index as user_index
from sitemap.views import index as website_index

def index(request):
	if request.user.is_authenticated():
		return user_index(request)
	else:
		return website_index(request)