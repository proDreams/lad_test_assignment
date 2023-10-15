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
        """
        Метод передачи в шаблон контекстных данных.
        Неочевидное место с передачей в шаблон формы оценки или оценки пользователя.
        Если пользователь авторизован, сперва проверяем, есть ли у него оценка книги.
        Если оценка есть, выводим его в шаблоне, если оценки нет, то выводим форму.
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = models.CommentModel.objects.filter(book=self.object)
        context['comment_form'] = forms.AddCommentForm()
        if self.request.user.is_authenticated:
            user_rating = models.BookRatingModel.objects.filter(user=self.request.user, book=self.get_object()).first()
            if user_rating:
                context['user_rating'] = user_rating
            else:
                context['rating_form'] = forms.BookRateForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Метод обработки POST-запросов.
        Если в пост запросе передана форма оценки книги, то создаём новый объект оценки.
        Если в пост запросе передана форма комментария, то создаём новый объект комментария.
        Иначе возвращаем обычный шаблон.
        """
        if 'rating' in request.POST:
            form = forms.BookRateForm(request.POST)
            if form.is_valid():
                rating = int(form.cleaned_data['rating'])
                book = self.get_object()
                models.BookRatingModel.objects.get_or_create(
                    user=request.user,
                    book=book,
                    defaults={'rating': rating}
                )
                return self.get(request, *args, **kwargs)
            else:
                context = self.get_context_data(**kwargs)
                context['rating_form'] = form
                return render(request, self.template_name, context)
        elif 'comment' in request.POST:
            form = forms.AddCommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.book = self.get_object()
                comment.user = request.user
                comment.save()
                return self.get(request, *args, **kwargs)
            else:
                context = self.get_context_data(**kwargs)
                context['comment_form'] = form
                return render(request, self.template_name, context)
        else:
            return self.get(request, *args, **kwargs)


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
