from django.shortcuts import render

from rest_framework import viewsets, permissions

from .serializers import CustomUserSerializer, AuthorSerializer, BookSerializer, OrderSerializer

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permissions_class = [
        permissions.AllowAny
    ]



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permissions_class = [
        permissions.AllowAny
    ]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_class = [
        permissions.AllowAny
    ]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions_class = [
        permissions.AllowAny
    ]
