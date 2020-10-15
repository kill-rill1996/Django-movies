from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie


class MoviesView(ListView):
    """List of films"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MoviewDetailView(DetailView):
    """Film detail, full description"""
    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

