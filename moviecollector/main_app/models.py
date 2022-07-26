from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Movie(models.Model):
    def __init__(self, title, year, actors, genre):
        self.title = title
        self.year = year
        self.actors = actors
        self.genre = genre
    user = models.ForeignKey(User, on_delete=models.CASCADE)

movies = [
    Movie('The Replacements', '2000', 'Keanu Reeves', 'comedy'),
    Movie('The Matrix', '1999', 'Laurence Fishborne, Keanu Reeves', 'Action, Sci Fi, Fantasy'),
    Movie('Friday', '1995', 'Ice Cube, Chris Tucker, John Witherspoon', 'Comedy')
]

