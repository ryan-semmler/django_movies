from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie, Rating
from operator import itemgetter


def index(request):
    template = loader.get_template('movielens_app/index.html')
    return HttpResponse(template.render())


def all_movies(request):
    movie_list = Movie.objects.all()
    context = {'movie_list': movie_list, }
    template = loader.get_template('movielens_app/all_movies.html')
    return HttpResponse(template.render(context, request))


def movie_detail(request, movie_id):
    m = Movie.objects.get(id=movie_id)
    movie_ratings = []
    for item in Rating.objects.filter(movie=movie_id):
        movie_ratings.append(item)
    total = 0
    for r in movie_ratings:
        total += r.rating
    average_rating = total / len(movie_ratings)
    context = {'m': m, 'average_rating': average_rating, 'ratings': len(movie_ratings), }
    template = loader.get_template('movielens_app/movie_detail.html')
    return HttpResponse(template.render(context, request))


def top_20(request):
    movies_and_ratings = {}
    movies_and_avg_ratings = []
    for r in Rating.objects.all():
        if r.movie in movies_and_ratings:
            movies_and_ratings[r.movie].append(r.rating)
        else:
            movies_and_ratings[r.movie] = [r.rating]
    for item in movies_and_ratings:
        if len(movies_and_ratings[item]) >= 10:
            x = movies_and_ratings[item]
            movies_and_avg_ratings.append((item, sum(x) / len(x)))
    movies_and_avg_ratings = sorted(movies_and_avg_ratings, key=itemgetter(1))
    movies_and_avg_ratings = movies_and_avg_ratings[:-21:-1]
    context = {'movies_and_avg_ratings': movies_and_avg_ratings, }
    template = loader.get_template('movielens_app/top_20.html')
    return HttpResponse(template.render(context, request))
