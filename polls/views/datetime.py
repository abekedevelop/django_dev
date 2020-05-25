from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
    html = "<html><body>It is now %s.</body></html>" % formatted_date
    return HttpResponse(html)