from django.db import models
from django.contrib.auth.models import User


class Rater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=25)
    age = models.IntegerField()
    zipcode = models.IntegerField()
    id = models.AutoField(primary_key=True)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    timestamp = models.IntegerField()

#
# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=30)
#     rater = models.OneToOneField(Rater, on_delete=models.CASCADE)
