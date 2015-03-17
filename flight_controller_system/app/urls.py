__author__ = 'carlos'

from django.conf.urls import patterns, url
from app.views import HomeView

urlpatterns = patterns(
    '',
    url(r'^/?$', HomeView.as_view())
)
