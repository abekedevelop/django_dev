from django.http import HttpResponseRedirect
from django.urls import reverse


def redirect_example(request):
    year = 2021

    return HttpResponseRedirect(reverse('polls:greet', args=(year,)))