from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from tastypie.resources import Resource
import json
from webserver.restapi.api import AlternativaResource
from webserver.restapi.models import User, Alternativa
import random

# def alternativas_list(self, request):
#     alt = AlternativaResource()
#     request_bundle = alt.build_bundle(request=request)
#     queryset = alt.obj_get_list(request_bundle)
#
#     bundles = []
#     for obj in queryset:
#         bundle = alt.build_bundle(obj=obj, request=request)
#         bundles.append(alt.full_dehydrate(bundle, for_list=True))
#
#     return bundles
#


def pick_alternativa(list):
    choice = random.choice(list)
    alt_result = choice
    return alt_result


def get_query_dict(request):
    index = int(request.GET.get('id'))
    user = User.objects.get(id=index)
    if user.alternativa is None:
        alternativas = Alternativa.objects.all()
        sorteio = pick_alternativa(alternativas)
        user.alternativa = sorteio
        user.save()

        ar = AlternativaResource()
        ar_bundle = ar.build_bundle(obj=user.alternativa, request=request)

        return HttpResponse(ar.serialize(request, ar.full_dehydrate(ar_bundle), format='application/json'))
    else:
        ar = AlternativaResource()
        ar_bundle = ar.build_bundle(obj=user.alternativa, request=request)
        return HttpResponse(ar.serialize(request, ar.full_dehydrate(ar_bundle), format='application/json'))
