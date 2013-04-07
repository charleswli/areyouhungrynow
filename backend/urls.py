from django.conf.urls.defaults import patterns, include, url
import views
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'helpers/sushi.json')
f = open(file_path)
sushi = f.readlines()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'areyouhungry.views.home', name='home'),
    # url(r'^areyouhungry/', include('areyouhungry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
    # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'views.home'),
                       url(r'^demo/search/sushi/*$', 'views.demo_sushi', {'sushi':sushi}),
                       url(r'^demo/search/*$', 'views.demo_search'),
                       url(r'^demo/business/yelp$', 'views.demo_yelp'),
                       url(r'^demo/business/(?P<business>([a-z]|-)*)$', 'views.demo_business'),
)
