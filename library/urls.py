from django.urls import path

from .views import AuthorListView, get_books, get_book, delete_book

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('api/v1/books/list', get_books),
    path('api/v1/books/by-<int:id>', get_book),
    path('api/v1/books/<int:id>', delete_book)
]