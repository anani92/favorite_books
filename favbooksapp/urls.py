from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome),
    path('addfav/<int:id>', views.add_favbook),
    path('<int:book_id>', views.view_book),
    path('add_to_favorites/<int:book_id>', views.add_to_favorites),
    path('remove_from_favorites/<int:book_id>', views.remove_from_favorites),
    path('edit_desc/<int:book_id>', views.edit_description),
    path('delete_book/<int:book_id>', views.delete_book),
    path('logout', views.log_out)
]
