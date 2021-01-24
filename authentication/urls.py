from django.urls import path
from .views import user_detail_view, users_listing_view, sign_in, sign_up

urlpatterns = [
    path('', users_listing_view, name="users_listing"),
    path('<int:pk>/', user_detail_view, name="user_details"),
    path('sign-in/', sign_in, name="user_sign_in"),
    path('sign-up/', sign_up, name="user_sign_up")
]
