from django.contrib import admin
from library.models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'name', 'time_create']
    list_display_links = ['id', 'photo', 'name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'name', 'time_create']
    list_display_links = ['id', 'photo', 'name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
