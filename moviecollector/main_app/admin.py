from django.contrib import admin
from .models import Movie, Ratings, Photo
# Register your models here.
admin.site.register(Movie)
admin.site.register(Ratings)
admin.site.register(Photo)
