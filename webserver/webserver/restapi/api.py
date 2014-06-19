from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from webserver.restapi.models import Experimento, Alternativa, User
# from webserver.restapi import views


class ExperimentoResource(ModelResource):
    ''' Classe resource representando o model Experimento. '''

    #relaciona objetos da classe AlternativaResource com a classe ExperimentoResource
    alternativas = fields.ToManyField('webserver.restapi.api.AlternativaResource', 'alternativas', related_name='alternativa', full=True)
    #users = fields.ToManyField('webserver.restapi.api.UserResource', 'users', full=True)

    class Meta:
        queryset = Experimento.objects.all()
        resource_name = 'experimento'
        filtering = {"name": ALL}
        authorization = Authorization()
        detail_uri_name = 'slug'

    #redefine a url do resource
    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<slug>[\w\.-]+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
            url(r'^experimento/$', 'webserver.restapi.views.get_query_dict')
        ]


class AlternativaResource(ModelResource):
    class Meta:
        queryset = Alternativa.objects.all()
        resource_name = 'alternativa'
        authorization = Authorization()
        excludes = ['id', 'resource_uri']


class UserResource(ModelResource):
    alternativa = fields.ForeignKey(AlternativaResource, 'alternativa', full=True, null=True)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        filtering = {'username': ALL, 'slug':ALL}

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<slug>[\w\.-]+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail')
        ]
