from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name='home-page'),
    path('filter/', views.MovieFilter.as_view(), name='filter-movie'),
    path('json-filter/', views.JsonFilterMoviesView.as_view(), name='json-filter'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('review/<int:pk>/', views.ReviewView.as_view(), name='add-review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor-detail'),


]
