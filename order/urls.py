from django.urls import path
from .views import orders_listing_view, order_detail_view, lended_books_views, create_order, update_order, delete_order

urlpatterns = [
    path('', orders_listing_view, name="order_listing"),
    path('<int:pk>/', order_detail_view, name="order_details"),
    path('open-orders', lended_books_views, name="lended_books"),
    path('create_order', create_order, name="create_order"),
    path('update_order/<int:pk>/', update_order, name="update_order"),
    path('delete_order/<int:pk>/', delete_order, name="delete_order"),
]




# path('create_order', create_order, name="create_order"), added 'create_order' path