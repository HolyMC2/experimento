from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Este es el indice configurado en views de aprendiendo")
