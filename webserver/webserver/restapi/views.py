from django.shortcuts import render
from django.http import HttpResponse
from webserver.restapi.api import AlternativaResource
from webserver.restapi.models import User, Alternativa, Experimento
import random


#sorteio (escolha aleatória) de uma alternativa
def pick_alternativa(experimento):
    alternativas = experimento.alternativas.all()
    choice = random.choice(alternativas)
    choice.sorteios += 1
    choice.save()
    return choice


#Busca a alternativa de um usuário ou sorteia uma nova
def get_query_dict(request, slug):
    index = int(request.GET.get('id'))
    experimento = Experimento.objects.get(slug=slug)
    user = User.objects.get(id=index)
    ar = AlternativaResource()
    #se o atributo estiver vazio, sorteia uma alternativa para o usuário
    if user.alternativa is None:
        sorteio = pick_alternativa(experimento)
        user.alternativa = sorteio
        user.save()

    ar_bundle = ar.build_bundle(obj=user.alternativa, request=request)

    return HttpResponse(ar.serialize(request, ar.full_dehydrate(ar_bundle), format='application/json'))


#Lista os testes cadastrados e o número de sorteios para cada alternativa
def dashboard(request):
    exp_list = Experimento.objects.all()
    context = {'exp_list': exp_list}
    return render(request, 'dash.html', context)
