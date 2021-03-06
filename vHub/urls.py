from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^', include('sitemap.urls', namespace='sitemap')),
    url(r'^videos/', include('app.urls', namespace='videos')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url='/static/favicon.ico',
        permanent=False
    )),
    url(r'', include('social_auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
