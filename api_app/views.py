
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .utils.graphqlclient import parameters
import json
from .models import Criature



# Create your views here.

def index(request):
    
    return HttpResponse("Hello Pokemon view.")


def evolution(request, id):

    elements = parameters(id)
    try:
        for element in elements:
            criature = Criature.objects.create(**element)
    except Exception as error:
        return HttpResponseBadRequest(f"<h3>There are little problem with {error}</h3>")

    # for element in elements:
    #     criature = Criature(
    #                     name= element['name'], 
    #                     baseStats= element['base_stats'], 
    #                     height= element['height'], 
    #                     weight= element['weight'],
    #                     evolutions= element['evolution'],
    #                     id_evolution= element['id_evolution']
    #     )
    #     criature.save()

    # import pdb; pdb.set_trace()  # debug

    return HttpResponse(
        json.dumps(elements, indent=4), 
        content_type='application/json',
        status=200
    )

def search(request, name):
    criature = Criature.objects.filter(name__iexact=name) # A case-insensitive match

    try:
        pokemon = criature[0]
        data = {
            'Evolution': pokemon.evolution,
            'Id': pokemon.id_evolution,
            'Name': pokemon.name
        }
        return HttpResponse(
            json.dumps(data, indent=4), 
            content_type='application/json'
        )
    except Exception as error:
        return HttpResponseBadRequest(f"<h3>There are little problem with {error}</h3>")

def ping(reques):
    return HttpResponse("pong")
