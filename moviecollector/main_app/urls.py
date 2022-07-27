from django.urls import path
from . import views
from main_app import views as main_app




urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movies_id>/', views.movies_detail, name='detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('accounts/signup/', main_app.signup, name='signup')
 
]