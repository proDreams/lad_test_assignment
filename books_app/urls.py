from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllBooksPage.as_view(), name='all_books'),
    path('book/<int:pk>/', views.BookPage.as_view(), name='book_page')
]
