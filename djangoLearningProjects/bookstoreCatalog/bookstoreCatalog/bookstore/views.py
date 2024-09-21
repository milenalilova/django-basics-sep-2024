from django.http import HttpResponse
from django.shortcuts import render

from bookstoreCatalog.bookstore.models import Book, Author, Genre, Review


def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()

    context = {
        'books': books,
        'authors': authors,
        'genres': genres
    }

    return render(request, 'bookstore/home_page.html', context)


def show_books_list(request):
    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'bookstore/books_list.html', context)


def show_book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}

    return render(request, 'bookstore/book_details.html', context)


def show_authors_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}

    return render(request, 'bookstore/authors_list.html', context)


def show_genres_list(request):
    genres = Genre.objects.all()
    context = {'genres': genres}

    return render(request, 'bookstore/genres_list.html', context)


def show_top_rated_books(request):
    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'bookstore/top_rated_books.html', context)


def show_recent_reviews(request):
    reviews = Review.objects.all()
    context = {'reviews': reviews}

    return render(request, 'bookstore/recent_reviews.html', context)
