from django.db import models
from django.contrib.auth.models import User


class Statement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    additional_data = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    file = models.FileField(upload_to='polls/images')

    class Meta:
        ordering = ['file']

    def __str__(self):
        return self.additional_data