from rest_framework.serializers import ModelSerializer

from books_app import models


class AllFilesSerializer(ModelSerializer):

    class Meta:
        model = models.BookModel
        fields = '__all__'
