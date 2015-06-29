from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^about/$', views.about, name='about'),
	url(r'^faq/$', views.faq, name='faq'),
	url(r'^tos/$', views.tos, name='tos'),
]