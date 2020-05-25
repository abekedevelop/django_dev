from django.http import HttpResponse
from django.views import View


class MyView(View):
    greeting = "Salamaleikum"

    def get(self, request):
        return HttpResponse(self.greeting)


class MorningGreetingView(MyView):
    greeting = 'Qalaisyn?'