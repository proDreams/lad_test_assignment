from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from api_app import serializers
from books_app import models


class AllBooksView(APIView):
    def get(self, *args, **kwargs):
        books = models.BookModel.objects.all()
        serialized_books = serializers.AllFilesSerializer(books, many=True)

        return Response(serialized_books.data)


class BookView(APIView):
    def get(self, *args, **kwargs):
        try:
            book = models.BookModel.objects.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            return Response({'error': 'Book not found'}, status=404)

        serialized_book = serializers.AllFilesSerializer(book)

        return Response(serialized_book.data)
