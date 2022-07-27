from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    actors = models.CharField(max_length=500)
    genre = models.TextField(max_length=100)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"movie_id":self.id})

    