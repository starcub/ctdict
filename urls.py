from django.conf.urls.defaults import *
import sys
import os.path 
from os.path import join
from ctdict import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    # static files
    (r'^css/(?P<path>.*)$', 'django.views.static.serve',{'document_root': join(settings.settings_path, 'dict/templates/css')}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve',{'document_root': join(settings.settings_path, 'dict/templates/images')}),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^term/(.*)', 'ctdict.dict.views.term'),
    (r'^ctdict/', 'ctdict.dict.views.index'),
    

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    
)
