from django.shortcuts import render
from django.http import HttpResponse
from webserver.restapi.api import AlternativaResource
from webserver.restapi.models import User, Alternativa, Experimento
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


def pick_alternativa(experimento):
    alternativas = experimento.alternativas.all()
    choice = random.choice(alternativas)
    choice.sorteios += 1
    choice.save()
    return choice


def get_query_dict(request, slug):
    index = int(request.GET.get('id'))
    experimento = Experimento.objects.get(slug=slug)
    user = User.objects.get(id=index)
    ar = AlternativaResource()
    if user.alternativa is None:
        sorteio = pick_alternativa(experimento)
        user.alternativa = sorteio
        user.save()

    ar_bundle = ar.build_bundle(obj=user.alternativa, request=request)

    return HttpResponse(ar.serialize(request, ar.full_dehydrate(ar_bundle), format='application/json'))


def dashboard(request):
    exp_list = Experimento.objects.all()
    context = {'exp_list': exp_list}
    return render(request, 'dash.html', context)
