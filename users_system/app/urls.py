__author__ = 'carlos'

from django.conf.urls import patterns, url
from app.views import HomeView, LoginView

urlpatterns = patterns(
    '',
    url(r'^/?$', HomeView.as_view()),
    url(r'^login', LoginView.as_view())
)
