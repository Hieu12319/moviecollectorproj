from django.urls import path
from . import views
from main_app import views as main_app




urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movies_id>/', views.movies_detail, name='detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('movies/<int:movies_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', main_app.signup, name='signup'),
]