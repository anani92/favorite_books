from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from login.models import User


def welcome(request):
    user_id = request.session['user_id']
    context = {
        "books": Book.objects.all(),
        'user': User.objects.get(id=user_id)

    }
    return render(request, 'books.html', context)


def add_favbook(request, id):
    user = User.objects.get(id=id)
    title = request.POST.get('book_title')
    description = request.POST.get('book_desc')
    new_book = Book.objects.create(
        title=title,
        description=description,
        uploaded_by=user
    )
    new_book.save()
    user.liked_books.add(new_book)
    return redirect('/books')


def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    context = {
        'book': book,
        'user': user
    }
    return render(request, 'showbook.html', context)


def add_to_favorites(request, book_id):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    user.liked_books.add(book)
    return redirect(f'/books')


def remove_from_favorites(request, book_id):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    user.liked_books.remove(book)
    return redirect(f'/books')


def edit_description(request, book_id):
    book = Book.objects.get(id=book_id)
    description = request.POST.get('desc_edit')
    book.description = description
    book.save()
    return redirect(f'/books/{book_id}')


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect(f'/books')


def log_out(request):
    request.session.clear()
    return redirect('/')
