from django.db import models
from login.models import User
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(
        User, related_name='uploaded_book', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(
        User, related_name='liked_books')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
