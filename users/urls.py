from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^app/', include('app.urls')),
    # url(r'^blog/', include('blog.urls')),
)
