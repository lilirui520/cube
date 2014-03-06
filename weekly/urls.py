from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    (r'^index/$', "weekly.views.index"),
    (r'^about/$', "weekly.views.about"),
    (r'^account/', include('accounts.urls')),
    (r'^report/', include('reports.urls')),
    (r'^$', "weekly.views.index"),
    # Examples:
    # url(r'^$', 'weekly.views.home', name='home'),
    # url(r'^weekly/', include('weekly.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    	(r'^admin/', include(admin.site.urls)),
)
