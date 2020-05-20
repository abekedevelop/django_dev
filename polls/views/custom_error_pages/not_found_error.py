from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


def not_found_handler(request, exception=None):
    rendered = render_to_string('polls/custom_error_pages/404_custom.html')
    response = HttpResponse(rendered)
    response.status_code = 404

    return response