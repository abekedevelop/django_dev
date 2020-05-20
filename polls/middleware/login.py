from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        current_url = request.resolver_match.url_name
        if not request.user.is_authenticated and current_url != 'index' and current_url != 'register':
            messages.add_message(request, messages.INFO, 'Please register or authorize')
            return redirect('polls:index')


        # Code to be executed for each request/response after
        # the view is called.

        return response


