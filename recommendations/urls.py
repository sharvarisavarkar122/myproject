from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie_search/', views.movie_search, name='movie_search'),
]
