from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import RedirectView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ashleytw.views.home', name='home'),
    # url(r'^ashleytw/', include('ashleytw.foo.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon1.ico')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
