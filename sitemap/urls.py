from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^tos/$', views.TosView.as_view(), name='tos'),
]
