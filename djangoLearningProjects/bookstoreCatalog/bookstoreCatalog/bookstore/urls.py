from django.urls import path

from bookstoreCatalog.bookstore import views

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.show_books_list, name='books list'),
    path('books/<int:pk>/', views.show_book_details, name='books details'),
    path('authors/', views.show_authors_list, name='authors list'),
    path('genres/', views.show_genres_list, name='genres list'),
    path('top_rated/', views.show_top_rated_books, name='top rated'),
    path('recent_reviews/', views.show_recent_reviews, name='recent reviews')
]
