from django.shortcuts import render, get_object_or_404
from .models import Movie, Series, Game, Review

def index(request):
    return render(request, 'home_screen.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def series_list(request):
    series = Series.objects.all()
    return render(request, 'series_list.html', {'series': series})

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review_detail.html', {'review': review})
