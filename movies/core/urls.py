from django.urls import path

from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name='home-page'),
    path('<slug:slug>/', views.MoviewDetailView.as_view(), name='movie-detail'),
    path('review/<int:pk>/', views.ReviewView.as_view(), name='add-review'),

]
