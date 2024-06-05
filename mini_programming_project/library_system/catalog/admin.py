from django.contrib import admin
from .models import Book, Magazine, Movie

admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(Movie)