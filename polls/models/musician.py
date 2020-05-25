from django.db import models
from django.urls import reverse


class Musician(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse('polls:musician_detail', kwargs={'pk':self.pk})