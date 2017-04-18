
from django.conf.urls import include, url
from django.contrib import admin
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^music/',include('music.urls')),
    url(r'^admin/', admin.site.urls)

]


# TODO: if it's in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


