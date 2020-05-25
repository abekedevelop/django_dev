from django.http import HttpResponse
from django.shortcuts import render


def greet(request, year):
    return HttpResponse("Hello %d" % year)