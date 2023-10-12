from django.shortcuts import render
from django.views.generic import ListView

from . import models


class AllBooksPage(ListView):
    model = models.BookModel
    template_name = "books_app/all_books.html"
    extra_context = {'title': 'Главная страница'}
    context_object_name = 'books'