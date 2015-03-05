from django.conf.urls import patterns, include, url
from general import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/$', views.index),
    url(r'^api/users/', include('users.urls'))
)
