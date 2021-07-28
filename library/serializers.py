from django.db.models import fields
from rest_framework import serializers
from .models import Author, Book


class BookWithAuthorNameSerialiser(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True, source="author.name")

    class Meta:
        model = Book
        fields = ['title', 'author']


class BookSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']


class AuthorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
