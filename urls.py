from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elecciones2012.views.home', name='home'),
    # url(r'^elecciones2012/', include('elecciones2012.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^municipio/$', 'town_graphs.views.index'),
    url(r'^municipio/(?P<municipio_id>\d+)/$', 'town_graphs.views.detail'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/mikel/open_data/elecciones2012/visualization/elecciones2012/town_graphs/static'}),
)
