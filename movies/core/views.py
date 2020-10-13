from django.shortcuts import render
from django.views.generic.base import View
from .models import Movie


class MoviesView(View):
    """List of films"""
    def get(self, request):
        movies = Movie.objects.all()
        context = {'movie_list': movies}
        return render(request, 'movies/movies.html', context)


class MoviewDetailView(View):
    """Film detail, full description"""
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        context = {'movie': movie}
        return render(request, 'movies/movie_detail.html', context)

