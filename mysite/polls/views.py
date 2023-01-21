from django.shortcuts import render
from django.http import HttpResponse #Renderiza texto

# Create your views here.

def index(request):
    return HttpResponse("Pantalla principal de la práctica")
