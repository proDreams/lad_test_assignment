from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView

from . import models, forms


class AllBooksPageView(ListView):
    model = models.BookModel
    template_name = "books_app/all_books.html"
    extra_context = {'title': 'Главная страница'}
    context_object_name = 'books'
    paginate_by = 6


class BookPageView(DetailView):
    model = models.BookModel
    template_name = "books_app/book_page.html"
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.CommentModel.objects.filter(book=self.object)
        context['form'] = forms.AddCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = forms.AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.get_object()
            comment.user = request.user
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return render(request, self.template_name, context)


class CommentUpdateView(UpdateView):
    model = models.CommentModel
    template_name = 'books_app/comment_edit.html'
    form_class = forms.EditCommentForm
    extra_context = {'title': 'Обновить комментарий?'}

    def get_success_url(self):
        return reverse_lazy('book_page',
                            kwargs={'pk': self.object.book.pk})


class CommentDeleteView(DeleteView):
    model = models.CommentModel
    template_name = 'books_app/confirm_delete_comment.html'
    extra_context = {'title': 'Удалить комментарий?'}

    def get_success_url(self):
        return reverse_lazy('book_page',
                            kwargs={'pk': self.object.book.pk})


@method_decorator(user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='editors').exists()),
                  name='dispatch')
class AddBookView(CreateView):
    model = models.BookModel
    form_class = forms.BookForm
    template_name = 'books_app/add_book.html'
    extra_context = {'title': 'Добавить книгу'}

    def get_success_url(self):
        return reverse_lazy('all_books')


@method_decorator(user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='editors').exists()),
                  name='dispatch')
class BookUpdateView(UpdateView):
    model = models.BookModel
    template_name = 'books_app/book_edit.html'
    form_class = forms.BookForm
    extra_context = {'title': 'Обновить книгу?'}

    def get_success_url(self):
        return reverse_lazy('book_page',
                            kwargs={'pk': self.object.pk})


@method_decorator(user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='editors').exists()),
                  name='dispatch')
class BookDeleteView(DeleteView):
    model = models.BookModel
    template_name = 'books_app/confirm_delete_book.html'
    extra_context = {'title': 'Удалить книгу?'}

    def get_success_url(self):
        return reverse_lazy('all_books')


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
