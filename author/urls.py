from django.urls import path
from .views import *

urlpatterns = [
    path('', author_listing_view, name="author_listing"),
    path('<int:pk>/', author_detail_view, name="author_details"),
    path('create_author/', createAuthor, name='create_author'),
    path('update_author/<int:pk>/', updateAuthor, name='update_author'),
    path('delete_author/<int:pk>/', deleteAuthor, name='delete_author'),
]
