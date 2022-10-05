from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt


def login_index(request):
    return render(request, 'index.html')


def register_user(request):
    errors = User.objects.validate_user(request)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        return redirect('/')

    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        new_user.save()
        request.session['user_id'] = new_user.id
        return redirect('/books')


def login_user(request):
    errors = User.objects.validate_login(request)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    email = request.POST.get('email')
    user = User.objects.filter(email=email)
    if user:
        request.session['user_id'] = user[0].id
        return redirect('/books')
