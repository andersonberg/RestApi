from django.conf.urls import patterns, include, url
from webserver.restapi.api import ExperimentoResource, UserResource, AlternativaResource

from django.contrib import admin
admin.autodiscover()
experimento_resource = ExperimentoResource()
user_resource = UserResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(experimento_resource.urls)),
    url(r'^api/', include(user_resource.urls)),
    url(r'^api/dashboard/$', 'webserver.restapi.views.dashboard'),
)
