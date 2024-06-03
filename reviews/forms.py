# forms.py
from django import forms
from .models import Movie, Series, Game, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date']

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['title', 'description', 'release_date']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'release_date']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'series', 'game', 'review_text', 'rating']
