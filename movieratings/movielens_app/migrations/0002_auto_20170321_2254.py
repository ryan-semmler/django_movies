# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 22:54
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 21:04
from __future__ import unicode_literals
from django.db import migrations
import csv
from ..models import Movie


class Migration(migrations.Migration):

    def load_movies(apps, schema_editor):
        with open('u.item', 'r', encoding='latin_1') as f:
            reader = csv.reader(f, delimiter="|")
            for row in reader:
                x = Movie()
                x.title = row[1]
                x.release_date = row[2]

    # def load_raters():
    #     with open(movielens_app/u.user, 'r') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             x = models.Rater
    #             x.occupation = row[3]
    #             x.age = row[1]
    #             x.gender = row[2]
    #             x.zipcode = row[4]
    #
    # def load_ratings():
    #     with open(movielens_app/u.data, 'r') as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             x = models.Rating
    #             x.movie = models.Movie.objects.get(id == row[1])[0]
    #             x.rater = models.Rater.objects.get(id == row[0])[0]
    #             x.rating = row[2]
    #             x.timestamp = row[3]


    dependencies = [
        ('movielens_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_movies),
        # migrations.RunPython(load_raters),
        # migrations.RunPython(load_ratings),
    ]
