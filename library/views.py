from django.shortcuts import render
from .models import author, book
from .serializers import bookSerialiser
from django.http import HttpResponse
from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

class AuthorListView(generic.ListView):
    model = author



@api_view(['GET'])
def books(request):
    print(book.objects.all().select_related())
    return Response(bookSerialiser(book.objects.all(), many=True).data)