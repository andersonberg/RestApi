from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from webserver.restapi.models import RestApi, Alternativa

#Classe resource representando o model RestApi
class RestApiResource(ModelResource):
    class Meta:
        queryset = RestApi.objects.all()
        resource_name = 'restapi'
        filtering = {"name": ALL}
        authorization = Authorization()
        detail_uri_name = 'slug'

    #redefine a url do resource
    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<slug>[\w\.-]+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]

class AlternativaResource(ModelResource):
    class Meta:
        queryset = Alternativa.objects.all()
        resource_name = 'alternativa'
        authorization = Authorization()