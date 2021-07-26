from django.db.models import fields
from rest_framework import serializers
from .models import author, book

class bookSerialiser(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True, source="author.name")
    class Meta:
        model = book
        fields = ['title', 'author']

class authorSerialiser(serializers.ModelSerializer):
    book = bookSerialiser(many=True, read_only=True)
    class Meta:
        model = author
        fields = ['name', 'book']