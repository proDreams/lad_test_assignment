from django.contrib import admin
from django.utils.html import format_html

from . import models


@admin.register(models.AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob',)
    search_fields = ('name',)


@admin.register(models.BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover_preview', 'author', 'publication_year')
    search_fields = ('title', 'author')

    def cover_preview(self, obj):
        """ Метод, добавляющий превью обложки на странице в админке """
        return format_html(f'<img src="{obj.book_cover.url}" width="100"/>')

    cover_preview.short_description = 'Обложка'
