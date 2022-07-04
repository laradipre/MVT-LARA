from django.shortcuts import render
from django.http import HttpResponse
from Mi_App.models import Familia, familia_paterna

def saludo (request):
    return HttpResponse("Bienvenido")

def familiares (request):
    context = {
        "familia": Familia.objects.all()
    }
    return render(request, "Mi_App/familia/index.html", context)

def familiacompleta (request):
    context = {
        "pariente": familia_paterna.objects.all()
    }
    return render (request, "Mi_App/familia_paterna/index.html", context)