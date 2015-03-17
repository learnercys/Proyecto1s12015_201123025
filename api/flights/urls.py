__author__ = 'carlos'

from django.conf.urls import patterns, url
from flights import views

urlpatterns = (
    url(r'/?', views.index)
)

