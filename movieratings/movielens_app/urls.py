from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all_movies$', views.all_movies, name='all_movies')
    # url(r'^top-20/?$', views.top_20, name='top_20'),
]
