from django.db import models


# Create your models here.
class BookModel(models.Model):
    bookname = models.CharField(max_length = 100)
    summary = models.TextField()
    rating = models.IntegerField()

class BookModel2(models.Model):
    bookname = models.CharField(max_length = 100)
    award = models.CharField(max_length = 30)
    year = models.IntegerField()
