from django.urls import path

from .views import AuthorListView, books 

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('api/v1/books/list', books)
]