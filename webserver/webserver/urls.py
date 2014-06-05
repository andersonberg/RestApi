from django.conf.urls import patterns, include, url
from webserver.restapi.api import RestApiResource

from django.contrib import admin
admin.autodiscover()
restapi_resource = RestApiResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(restapi_resource.urls)),
)
