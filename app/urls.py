from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/$',
        views.DetailView.as_view(),
        name='detail'
    ),

    url(
        r'^add/$',
        views.AddView.as_view(),
        name='add'
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
        r'^videos/$',
        views.VideosView.as_view(),
        name='videos'
    ),

     url(
        r'^detail/$',
        views.DetailView.as_view(),
        name='detail'
    ),
]
