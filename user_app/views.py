from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_app.forms import LoginForm, RegistrationForm


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'user_app/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('all_books')


class CustomRegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'user_app/signup.html'
    extra_context = {'title': 'Регистрация на сайте'}

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
