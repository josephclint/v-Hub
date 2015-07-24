from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),

    url(
        r'^(?P<pk>\d+)/$',
        views.DetailView.as_view(),
        name='detail'
    ),

    url(
        r'^upload/$',
        views.UploadView.as_view(),
        name='upload'
    ),

    url(
        r'^followers/$',
        views.FollowersView.as_view(),
        name='followers'
    ),

    url(
        r'^following/$',
        views.FollowingView.as_view(),
        name='following'
    ),

    url(
        r'^add_comment/$',
        views.AddComment.as_view(),
        name='add_comment'
    ),

    url(
        r'^home/$',
        views.HomeView.as_view(),
        name='home'
    ),
]
