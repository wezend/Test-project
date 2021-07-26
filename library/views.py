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
def get_books(request):
    return Response(bookSerialiser(book.objects.all(), many=True).data)

@api_view(['GET'])
def get_book(request, id):
    try: 
        return Response(bookSerialiser(book.objects.get(id = id)).data)
    except book.DoesNotExist:
        return Response('Wrong id')

@api_view(['POST'])
def update_book(request):
    try:
        updatedBook = book.objects.get(id = request.data['id'])
        if 'title' in request.data:
            updatedBook.title = request.data['title']
        if 'author' in request.data:
            updatedBook.author = author.objects.get(id = request.data['author'])
        updatedBook.save()
        return Response('Success')
    except book.DoesNotExist:
        return Response('Unsuccess')

@api_view(['DELETE'])
def delete_book(request, id):
    try:
        book.objects.get(id = id).delete() 
        return Response('Success')
    except book.DoesNotExist:
        return Response('Wrong id')