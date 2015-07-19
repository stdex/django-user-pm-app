from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^discussions/', include('discussions.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', 'project_example.views.root', name='root'),    
)
