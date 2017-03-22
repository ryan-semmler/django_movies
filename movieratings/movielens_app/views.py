from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie

def index(request):
    template = loader.get_template('movielens_app/index.html')
    return HttpResponse(template.render())

def all_movies(request):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list, }
    template = loader.get_template('movielens_app/all_movies.html')
    return HttpResponse(template.render(context, request))