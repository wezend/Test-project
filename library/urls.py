from django.urls import path

from .views import BooksList, BookById, UpdateBook, DeleteBook, CreateBook, CreateAuthor

urlpatterns = [
    path('books/list', BooksList.as_view()),
    path('books/by-<int:id>', BookById.as_view()),
    path('books/update<int:id>', UpdateBook.as_view()),
    path('books/<int:id>', DeleteBook.as_view()),
    path('books', CreateBook.as_view()),
    path('authors', CreateAuthor.as_view())
]
