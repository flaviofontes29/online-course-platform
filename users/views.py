from django.shortcuts import render
from django.http import HttpResponse


def registration(request):
    return HttpResponse("Página de cadastro")


def login(request):
    return HttpResponse("Página Login")
