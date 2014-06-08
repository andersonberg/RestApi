from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from webserver.restapi.models import RestApi, Alternativa, User

#Classe resource representando o model RestApi
class RestApiResource(ModelResource):
    #relaciona objetos da classe AlternativaResource com a classe RestApiResource
    alternativas = fields.ToManyField('webserver.restapi.api.AlternativaResource', 'alternativas', related_name='alternativa', full=True)
    users = fields.ToManyField('webserver.restapi.api.UserResource', 'users', full=True)
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
        excludes = ['id', 'resource_uri']

class UserResource(ModelResource):
    alternativa = fields.ForeignKey(AlternativaResource, 'alternativa', full=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        filtering = {'username': ALL}
