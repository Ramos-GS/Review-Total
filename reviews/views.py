from .models import Movie, Series, Game, Review
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm, SeriesForm, GameForm, ReviewForm

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

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form})

def add_series(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('series_list')
    else:
        form = SeriesForm()
    return render(request, 'add_series.html', {'form': form})

def edit_series(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    if request.method == 'POST':
        form = SeriesForm(request.POST, instance=series)
        if form.is_valid():
            form.save()
            return redirect('series_list')
    else:
        form = SeriesForm(instance=series)
    return render(request, 'edit_series.html', {'form': form})

# Game views
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})

def edit_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'edit_game.html', {'form': form})