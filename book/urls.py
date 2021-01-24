from django.urls import path
from .views import *


urlpatterns = [
    path('', book_listing_view, name="book_listing"),
    path('<int:pk>/', book_detail_view, name="book_details"),
    path('create_book/', createBook, name='create_book'),
    path('update_book/<int:pk>/', updateBook, name='update_book'),
    path('delete_book/<int:pk>/', deleteBook, name='delete_book'),
]