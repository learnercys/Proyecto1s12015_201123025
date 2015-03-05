__author__ = 'carlos'

from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns(
    '',
    url(r'^create/?$',  views.create),
    url(r'^delete/?$', views.delete),
    url(r'^login/?$', views.login),
    url(r'^logout/?$', views.logout)
)