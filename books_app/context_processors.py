from . import forms


def get_search_form(request):
    """ Контекстный процессор, передающий во все шаблоны форму поиска """
    return {'search_form': forms.SearchForm()}
