from django.db import models
import re
import bcrypt


class UserManger(models.Manager):
    def validate_user(self, request_data):
        errors = {}
        email = request_data.POST.get('email')
        users = User.objects.filter(email=email)
        if request_data.POST.get('first_name') and len(request_data.POST.get('first_name')) < 5:
            errors['first_name'] = 'username should be at least 5 letters'
        if request_data.POST.get('last_name') and len(request_data.POST.get('first_name')) < 5:
            errors['last_name'] = 'lastname should be at least 5 letters'
        if len(email) < 15:
            errors['email'] = 'email should be at least 15 letters'
        if len(request_data.POST['password']) < 8:
            errors["password"] = "The Password should be at least 8 characters"
        if request_data.POST['password'] != request_data.POST.get('confirm_password') and request_data.POST.get('confirm_password'):
            errors['password'] = 'password does not match'
        EMAIL_REGEX = re.compile(
            '^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Invalid email format"
        if len(users) > 0:
            errors['user_exist'] = 'User with this email already exist!'
        return errors

    def validate_login(self, request_date):
        errors = {}
        email = request_date.POST.get('email')
        password = request_date.POST.get('password')
        user = User.objects.filter(email=email)
        EMAIL_REGEX = re.compile(
            '^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Invalid email format"

        if user:
            if bcrypt.checkpw(password.encode(), user[0].password.encode()) == False:
                errors['password'] = 'username or password does not match'
        else:
            errors['user_email'] = 'User with this email doesn\'t exist'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=95)
    password = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManger()
