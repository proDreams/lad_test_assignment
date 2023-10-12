from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from . import models, forms


class AllBooksPage(ListView):
    model = models.BookModel
    template_name = "books_app/all_books.html"
    extra_context = {'title': 'Главная страница'}
    context_object_name = 'books'


class BookPage(DetailView):
    model = models.BookModel
    template_name = "books_app/book_page.html"
    context_object_name = 'book'


class SearchPageView(TemplateView):
    template_name = 'books_app/search.html'

    def get(self, request, *args, **kwargs):
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            books = (models.BookModel.objects.filter(title__icontains=query) |
                     models.BookModel.objects.filter(author__name__icontains=query))
            paginator = Paginator(books, 10)
            page_number = request.GET.get('page', 1)
            results = paginator.get_page(page_number)

            context = {"query": query,
                       "results": results}

            return render(request,
                          self.template_name,
                          context)

        return render(request,
                      self.template_name,
                      {"query": request.GET['query']})
