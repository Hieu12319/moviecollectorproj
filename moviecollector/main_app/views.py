from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .models import Movie

#class Movie:
#    def __init__(self, title, year, actors, genre):
#        self.title = title
#        self.year = year
#        self.actors = actors
#        self.genre = genre

 
#movies = [
#   Movie('The Replacements', '2000', 'Keanu Reeves', 'comedy'),
#    Movie('The Matrix', '1999', 'Laurence Fishborne, Keanu Reeves', 'Action, Sci Fi, Fantasy'),
#    Movie('Friday', '1995', 'Ice Cube, Chris Tucker, John Witherspoon', 'Comedy')
#]





def home(request):
    return HttpResponse('<h1> Hello World </h1>')


def about(request):
    return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'Movie': movies})


def movies_detail(request, movies_id):
    movie = Movie.objects.get(id=movies_id)
    return render(request, 'movies/detail.html', {'movies': movie})


class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'year', 'actors', 'genre']
    success_url = '/movies/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
