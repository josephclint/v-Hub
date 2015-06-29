from django.conf.urls import url
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^(?P<video_id>\d+)/$', views.detail, name='detail'),
	url(r'^add/$', views.add, name='add'),
]