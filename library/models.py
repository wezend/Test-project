from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class author(models.Model):
    name = CharField(max_length=15)

    def __str__(self):
        return self.name

class book(models.Model):
    author = models.ForeignKey(
        author,
        on_delete=CASCADE
    )
    title = CharField(max_length=15)

    def __str__(self):
        return self.title
        