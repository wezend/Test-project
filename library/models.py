from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models import Count
# Create your models here.


class Author(models.Model):
    name = CharField(max_length=15)

    def __str__(self):
        return self.name

    def number_of_books(self):
        return self.book_set.count()


class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=CASCADE
    )
    title = CharField(max_length=15)

    def __str__(self):
        return self.title
