from django.urls import path
from . import views

urlpatterns = [
    path('authors/all', views.AuthorListView.as_view(), name='author-list'),
    path('authors/<int:author_id>/detail/', views.AuthorDetailView.as_view(), name='author-delete'),
    path('authors/<int:author_id>/update/', views.AuthorUpdateView.as_view(), name='author-delete'),
    path('authors/<int:author_id>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
    path('authors/', views.AuthorView.as_view(), name='author-add'),
    path('authors/<int:author_id>/books/', views.BookView.as_view(), name='book-add'),
    path('authors/<int:author_id>/books/all/', views.AuthorBooksView.as_view(), name='author-books'),
    path('authors/<int:author_id>/books/<int:book_id>/', views.BookDeleteView.as_view(), name='book-delete'),
    path('authors/<int:author_id>/books/<int:book_id>/detail/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/<int:author_id>/books/<int:book_id>/update/', views.BookUpdateView.as_view(), name='book-update'),
]