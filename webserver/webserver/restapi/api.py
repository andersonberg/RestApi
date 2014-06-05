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

class AlternativaResource(ModelResource):
    class Meta:
        queryset = Alternativa.objects.all()
        resource_name = 'alternativa'
        authorization = Authorization()