from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ashleytw.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^gallery/$', gallery),
    url(r'^video/$', video),
    url(r'^forum/$', forum),
    url(r'^family-tree/$', family_tree),
    url(r'^contact/$', contact),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'home.html'}, name='logout'),
    url(r'profile', profile),
    # url(r'^ashleytw/', include('ashleytw.foo.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon1.ico')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()


