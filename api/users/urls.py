__author__ = 'carlos'

from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns(
    '',
    url(r'^create/$',  views.create_user),
    url(r'^delete/$', views.delete_user)
)