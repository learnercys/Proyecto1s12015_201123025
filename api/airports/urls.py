__author__ = 'carlos'

from django.conf.urls import patterns, url
from airports import views

urlpatterns = patterns(
    '',
    url(r'^/?$', views.index),
    url(r'^create/?$', views.create)
)
