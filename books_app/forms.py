from django import forms


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
