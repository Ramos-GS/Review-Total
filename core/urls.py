from django.contrib import admin
from django.urls import path
from reviews import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/add/', views.add_movie, name='add_movie'),
    path('movies/edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('series/', views.series_list, name='series_list'),
    path('series/add/', views.add_series, name='add_series'),
    path('series/edit/<int:series_id>/', views.edit_series, name='edit_series'),
    path('games/', views.game_list, name='game_list'),
    path('games/add/', views.add_game, name='add_game'),
    path('games/edit/<int:game_id>/', views.edit_game, name='edit_game'),
    path('reviews/<int:review_id>/', views.review_detail, name='review_detail'),
]

