from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    (r'^mine/$', "reports.views.mine"),
    (r'^all/$', "reports.views.all"),
    # Examples:
    # url(r'^$', 'weekly.views.home', name='home'),
    # url(r'^weekly/', include('weekly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
