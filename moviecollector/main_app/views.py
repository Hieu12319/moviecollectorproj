from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RatingsForm
from django.views.generic import ListView, DetailView

from .models import Movie, Ratings, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'moviecollect-hn-89'


def home(request):
    return HttpResponse('<h1> Hello World Welcome to My Movies APP </h1>')


def about(request):
    return render(request, 'about.html')


def movies_index(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/index.html', {'Movie': movies})


def movies_detail(request, movies_id):
    movie = Movie.objects.get(id=movies_id)
    ratings_form = RatingsForm()
    return render(request, 'movies/detail.html', {'movies': movie, 'ratings_form': RatingsForm})
    
def add_ratings(request, movies_id):
    form = RatingsForm(request.POST)
    if form.is_valid():
        new_ratings = form.save(commit=False)
        new_ratings.movies_id = movies_id
        new_ratings.save()
    return redirect('detail', movies_id= movies_id)

def assoc_ratings(request, movies_id, ratings_id):
    Movie.objects.get(id=movies_id).ratings.add(ratings_id)
    return redirect('detail', movies_id=movies_id)


@login_required
def add_photo(request, movies_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, movies_id=movies_id)
            photo.save()
        except:
            print('An error occored while uploading file to S3')
    return redirect('detail', movies_id=movies_id)


class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'year', 'actors', 'genre']
    success_url = '/movies/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'year', 'actors', 'genre']


class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'

class RatingsList(ListView):
    model = Ratings

class RatingsDetail(DetailView):
    model = Ratings

class RatingsCreate(CreateView):
    model = Ratings
    fields = '__all__'

class RatingsUpdate(UpdateView):
    model = Ratings
    fields = ['thoughts', 'rate']

class RatingsDelete(DeleteView):
    model = Ratings
    success_url = '/ratings/'




def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
