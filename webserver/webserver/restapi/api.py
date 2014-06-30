from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization
from tastypie import fields
from webserver.restapi.models import Experimento, Alternativa, User
# from webserver.restapi import views


class ExperimentoResource(ModelResource):
    """ Classe resource que corresponde ao modelo Experimento. """

    #relaciona objetos da classe AlternativaResource com a classe ExperimentoResource
    alternativas = fields.ToManyField('webserver.restapi.api.AlternativaResource', 'alternativas', related_name='alternativa', full=True)

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
            #padrão de url para requisitar um sorteio para um usuário específico
            url(r'^experimento/(?P<slug>[\w\.-]+)/user/$', 'webserver.restapi.views.get_query_dict')
        ]


class AlternativaResource(ModelResource):
    """ Classe resource que corresponde ao modelo Alternativa. """
    class Meta:
        queryset = Alternativa.objects.all()
        resource_name = 'alternativa'
        authorization = Authorization()
        excludes = ['id', 'resource_uri']


class UserResource(ModelResource):
    """ Classe resource que corresponde ao modelo User. """
    #um usuário tem somente uma alternativa, obtida através de um sorteio (escolha aleatória)
    alternativa = fields.ForeignKey(AlternativaResource, 'alternativa', full=True, null=True)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        filtering = {'username': ALL, 'slug': ALL}

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>%s)/(?P<slug>[\w\.-]+)/$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail')
        ]
