from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
RATES = (
    ('1', 'Loved it'),
    ('2', 'it is ok'),
    ('3', 'Fell asleep while watching')
)
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    actors = models.CharField(max_length=500)
    genre = models.TextField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"movies_id":self.id})

class Ratings(models.Model):
    thoughts = models.CharField(max_length=500)
    rate = models.CharField(
        max_length=10,
        choices=RATES,
        default=RATES[0][0]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.get_rate_display()} on {self.thoughts}"

class Photo(models.Model):
    url = models.CharField(max_length=300)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for movies_id: {self.movies_id} @{self.url}"