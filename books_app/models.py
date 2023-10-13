from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class AuthorModel(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Имя автора')
    dob = models.DateField(verbose_name='Дата рождения')
    short_bio = models.CharField(max_length=500,
                                 verbose_name='Краткая биография')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class BookModel(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Название книги')
    author = models.ForeignKey('AuthorModel',
                               on_delete=models.CASCADE,
                               verbose_name='Автор книги')
    publication_year = models.IntegerField(verbose_name='Дата публикации')
    short_description = models.CharField(max_length=500,
                                         verbose_name='Краткое описание')
    book_cover = models.ImageField(upload_to='books/',
                                   default='default.png',
                                   verbose_name='Обложка')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('book_page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    book = models.ForeignKey('BookModel',
                             on_delete=models.CASCADE,
                             verbose_name='Книга')
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий от {self.user} к книге {self.book}'
