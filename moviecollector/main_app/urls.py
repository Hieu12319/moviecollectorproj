from django.urls import path
from . import views
from main_app import views as main_app




urlpatterns = [
    path('about/', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movies_id>/', views.movies_detail, name='detail'),
    path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
    path('movies/<int:movies_id>/add_ratings/', views.add_ratings, name='add_ratings'),
    path('movies/<int:movies_id>/assoc_ratings/<int:ratings_id>/', views.assoc_ratings, name='assoc_ratings'),
    path('movies/<int:movies_id>/add_photo/', views.add_photo, name='add_photo'),
    path('ratings/', views.RatingsList.as_view(), name='ratings_index'),
    path('ratings/<int:pk>/', views.RatingsDetail.as_view(), name='ratings_detail'),
    path('ratings/create/', views.RatingsCreate.as_view(), name='ratings_create'),
    path('ratings/<int:pk>/update/', views.RatingsUpdate.as_view(), name='ratings_update'),
    path('ratings/<int:pk>/delete/', views.RatingsDelete.as_view(), name='ratings_delete'),
    path('accounts/signup/', main_app.signup, name='signup'),
]