from django import forms

from books_app import models


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control me-2 mx-1',
                                    'placeholder': 'Что ищем?',
                                }
                            ))

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
