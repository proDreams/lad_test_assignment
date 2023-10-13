from django.urls import path

from api_app import views

urlpatterns = [
    path('all_books/', views.AllBooksView.as_view(), name='all_books'),
    path('get_book/<int:pk>', views.BookView.as_view(), name='get_book'),
]