from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllBooksPage.as_view(), name='all_books'),
    path('book/<int:pk>/', views.BookPage.as_view(), name='book_page'),
    path('search/', views.SearchPageView.as_view(), name='search_page'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
