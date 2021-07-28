from django.shortcuts import render
from .models import Author, Book
from .serializers import BookSerialiser, AuthorSerialiser, BookWithAuthorNameSerialiser
from django.http import HttpResponse
from django.views import generic
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


class AuthorListView(generic.ListView):
    model = Author


class BooksList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookWithAuthorNameSerialiser


class BookById(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser
    lookup_field = 'id'


class UpdateBook(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser
    lookup_field = 'id'


class DeleteBook(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser
    lookup_field = 'id'


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser


class CreateAuthor(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerialiser
