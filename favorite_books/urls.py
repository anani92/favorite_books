
from django.urls import path, include

urlpatterns = [
    path('', include('login.urls')),
    path('books/', include('favbooksapp.urls')),
]
