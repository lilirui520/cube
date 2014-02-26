from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gelievable.views.home', name='home'),
    # url(r'^gelievable/', include('gelievable.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'login/$', 'accounts.views.login_view'),
    url(r'login/$', login),
    url(r'logout/$', logout),
    url(r'register/$', 'accounts.views.register_view'),
)
