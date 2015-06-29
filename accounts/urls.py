from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(
		r'^$',
		views.index,
		name='index',
	),
	url(
		r'^login/$', 
		auth_views.login, 
		{'template_name': 'accounts/login.html'}, 
		name='login',
	),
	url(
		r'^logout/$', 
		auth_views.logout, 
		{'template_name': 'accounts/logout.html'}, 
		name='logout',
	),
	url(
		r'^password_change/$', 
		auth_views.password_change, 
		{'template_name': ''}, 
		name='password_change',
	),
	url(
		r'^password_change/done/$', 
		auth_views.password_change_done, 
		{'template_name': ''}, 
		name='password_change_done',
	),
	url(
		r'^password_reset/$', 
		auth_views.password_reset, 
		{'template_name': ''}, 
		name='password_reset',
	),
	url(
		r'^password_reset/done/$', 
		auth_views.password_reset_done, 
		{'template_name': ''}, 
		name='password_reset_done',
	),
	url(
		r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
		auth_views.password_reset_confirm, 
		{'template_name': ''}, 
		name='password_reset_confirm',
	),
	url(
		r'^reset/done/$', 
		auth_views.password_reset_complete, 
		{'template_name': ''}, 
		name='password_reset_complete',
	),
	url(
		r'^signup/$',
		views.signup,
		name='signup',
	),
	url(
		r'^registration_complete$',
		views.post_register,
		name='post_register'
	),
]