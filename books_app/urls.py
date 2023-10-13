from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllBooksPageView.as_view(), name='all_books'),
    path('book/<int:pk>/', views.BookPageView.as_view(), name='book_page'),
    path('book/add/', views.AddBookView.as_view(), name='add_book'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('search/', views.SearchPageView.as_view(), name='search_page'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
