from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datasploit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('homepage.urls', namespace="homepage")),
    url(r'^facebook/',include('facebook.urls', namespace="facebook")),
)
