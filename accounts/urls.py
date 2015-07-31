from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^login/$', views.anonymous_required(auth_views.login),
        {'template_name': 'accounts/login.html'}, name='login'),

    url(r'^logout/$', auth_views.logout,
        {'template_name': 'accounts/logout.html'}, name='logout'),

    url(r'^password_change/$', views.ChangePasswordView.as_view(),
        name='password_change'),

    url(r'^password_change/done/$', auth_views.password_change_done,
        {'template_name': ''}, name='password_change_done'),

    url(r'^password_reset/$', auth_views.password_reset,
        {
            'template_name': 'accounts/password_reset.html',
            'post_reset_redirect': '/password_reset/done/',
        }, name='password_reset'),

    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'accounts/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/ \
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': ''}, name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': ''}, name='password_reset_complete'),

    url(r'^signup/$', views.SignupView.as_view(), name='signup'),

    url(r'^registration_complete$', views.PostRegisterView.as_view(),
        name='post_register'),

    url(r'^profile/$', views.UserProfileView.as_view(),
        name='user_profile'),

    url(r'^profile/edit/$', views.EditProfileView.as_view(),
        name='edit_profile'),

    url(r'^profile/(?P<pk>\w+)/$', views.ProfileView.as_view(),
        name='profile'),

    url(r'^deactivate/$', views.DisableAccountView.as_view(),
        name='deactivate'),

    url(r'^settings/$', views.SettingsView.as_view(), name='settings'),

]
