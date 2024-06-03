from django.contrib import admin
from django.urls import path
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('movies/', views.movie_list, name='movie_list'),
    path('series/', views.series_list, name='series_list'),
    path('games/', views.game_list, name='game_list'),
    path('review/<int:review_id>/', views.review_detail, name='review_detail'),
]
