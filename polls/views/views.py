from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from polls.models import Choice, Question
from django.views import generic
from django.utils import timezone

from ..forms import RegisterForm
from django.db import IntegrityError
import logging
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = RegisterForm()

    return render(request, 'polls/register.html', {'form': form})


def registered(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    password_confirmation = request.POST['confirm_password']

    if password != password_confirmation:
        messages.add_message(request, messages.INFO, 'Passwords do not match!')
        return HttpResponseRedirect(reverse('polls:register', ), request)

    try:
        User.objects.create_user(name, email, password)
    except IntegrityError as e:
        logger = logging.getLogger(__name__)
        logger.error(e.__cause__)
        messages.add_message(request, messages.INFO, 'Same user already exists')

        return HttpResponseRedirect(reverse('polls:register',), request)

    return HttpResponse("U are registered as {0} {1}".format(name, email))


def authenticate(request):
    form = AuthenticationForm()

    return render(request, 'polls/authentication.html', {'form': form})


