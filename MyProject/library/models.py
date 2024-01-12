from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.PositiveIntegerField()
    is_borrowed = models.BooleanField(default=False)

class Reader(models.Model):
    name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book)
