from django.shortcuts import render
from .models import author, book
from django.http import HttpResponse
from django.views import generic
# Create your views here.

class AuthorListView(generic.ListView):
    model = author