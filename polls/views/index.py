from django.db import models

from django.http import HttpResponse


def index_page(request):
    return HttpResponse('index page')