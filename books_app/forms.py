from django import forms

from books_app import models


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control me-2 mx-1',
                'placeholder': 'Что ищем?',
            }
        )
    )

    def clean_query(self):
        """
        Переопределённый метод очистки поля query.
        Удаляет лишние пробелы внутри текста.
        """
        query = self.cleaned_data['query']
        cleaned_query = " ".join(query.split())
        return cleaned_query


class AddCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш комментарий.',
                'rows': 5,
            }
        )
    )

    class Meta:
        model = models.CommentModel
        fields = ['comment']


class EditCommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш комментарий.',
                'rows': 5,
            }
        )
    )

    class Meta:
        model = models.CommentModel
        fields = ['comment']


class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50,
        label='Название книги',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите название книги.',
            }
        )
    )
    author = forms.ModelChoiceField(
        label='Автор книги',
        queryset=models.AuthorModel.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            }
        )
    )
    publication_year = forms.IntegerField(
        label='Год издания книги',
        max_value=2035,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите год издания книги.',
            }
        )
    )
    short_description = forms.CharField(
        label='Короткое описание',
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите краткое описание книги.',
                'rows': 3,
            }
        )
    )
    book_cover = forms.FileField(
        label='Обложка книги',
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = models.BookModel
        fields = ['title', 'author', 'publication_year', 'short_description', 'book_cover']
