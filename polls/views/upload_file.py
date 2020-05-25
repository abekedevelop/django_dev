from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from ..forms import UploadFileForm, StatementForm
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth.models import  User


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request, request.FILES['file'])
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = UploadFileForm()
    return render(request, 'polls/upload_file.html', {'form': form})


def handle_uploaded_file(request, f):
    filename = request.POST['title']
    with open(filename + '.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# @require_http_methods(['POST'])
def model_file_upload(request):
    if request.method == 'POST':
        form = StatementForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = User.objects.get(pk=5)
                statement = form.save(commit=False)
                statement.user = user
                statement.save()
            except Exception as e:
                messages.add_message(request, messages.ERROR, str(e))

        messages.add_message(request, messages.ERROR, 'File uploaded successfully')
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        form = StatementForm()
    return render(request, 'polls/statement_form.html', {'form': form,})