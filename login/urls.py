from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_index),
    path('register', views.register_user),
    path('login', views.login_user)
]
