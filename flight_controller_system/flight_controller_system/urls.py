from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flight_controller_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'/?', include('app.urls'))
)
