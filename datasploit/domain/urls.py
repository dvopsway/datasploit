from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'domain.views.module_page' , name='home'),
    url(r'^search/', 'domain.views.search' , name='search'),
]
