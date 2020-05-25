from polls.models import Musician
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render


class MusicianCreate(CreateView):
    model = Musician
    template_name = 'polls/class_based/musician_create.html'
    context_object_name = 'musician'
    fields = ['name', 'age']

    # def post(self, request, *args, **kwargs):
    #     print('post received')
    #     return HttpResponseRedirect(reverse('polls:index'))
    #
    def form_valid(self, form):
        model = form.save()

        return HttpResponseRedirect(reverse('polls:musician_detail', kwargs={'pk':model.id}))


class MusicianUpdate(UpdateView):
    model = Musician
    template_name = 'polls/class_based/musician_update.html'
    fields = ['name', 'age']


class MusicianDelete(DeleteView):
    model = Musician
    template_name = 'polls/class_based/musician_delete.html'
    success_url = reverse_lazy('polls:index')


class MusicianDetail(DetailView):
    model = Musician
    template_name = 'polls/class_based/musician_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MusicianList(ListView):
    model = Musician
    template_name = 'polls/class_based/musician_list.html'
