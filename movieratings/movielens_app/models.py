from django.db import models


class Rater(models.Model):
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=25)
    age = models.IntegerField()
    zipcode = models.IntegerField()
    id = models.AutoField(primary_key=True)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)


class Rating(models.Model):
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    timestamp = models.IntegerField()
