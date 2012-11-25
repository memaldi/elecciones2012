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
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/mikel/open_data/elecciones2012/elecciones2012/town_graphs/static'}),
)

#My code

import urllib
import json
from town_graphs.models import Municipio

municipios = Municipio.objects.all()

for municipio in municipios:
    if None in [municipio.lat, municipio.long]:
        params = urllib.urlencode({'name': municipio.name.encode('utf-8'), 'type': 'json', 'username': 'memaldi'})
        response = urllib.urlopen('http://api.geonames.org/search?%s' % params)
        json_response = json.loads('[' + response.read() + ']')
        #print json_response[0]
        done = False
        if json_response[0]['totalResultsCount'] > 0:
            for item in json_response[0]['geonames']:
                if item['countryName'] == 'Spain':
                    municipio.lat = item['lat']
                    municipio.long = item['lng']
                    municipio.save()
                    done = True
                    break;
        if not done:
            print municipio.name, municipio.id
