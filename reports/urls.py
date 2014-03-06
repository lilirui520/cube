from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    (r'^index/$', "reports.views.index"),
    (r'^new/$', "reports.views.new"),
    (r'^all/$', "reports.views.all"),
    #(r'^post/$', "reports.views.post"),
    # Examples:
    # url(r'^$', 'weekly.views.home', name='home'),
    # url(r'^weekly/', include('weekly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
