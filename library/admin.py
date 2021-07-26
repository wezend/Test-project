from django.contrib import admin
from .models import author, book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_books')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

admin.site.register(author, AuthorAdmin)
admin.site.register(book, BookAdmin)