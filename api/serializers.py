from rest_framework import serializers

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "password",
            "updated_at",
            "created_at",
            "role",
            "is_active",
            "is_staff",
            "url"
        ]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "surname",
            "patronymic",
            "url"
        ]


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='author-detail'
    )
    class Meta:
            model = Book
            fields = [
                "id",
                "name",
                "description",
                "count",
                "authors",
                "url"
            ]


class OrderSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    book = BookSerializer()
    class Meta:
            model = Order
            fields = (
                "id",
                "user",
                "book",
                "created_at",
                "end_at",
                "plated_end_at",
                "url"
            )
