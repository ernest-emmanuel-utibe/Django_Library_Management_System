from rest_framework import serializers
from book.models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # todo relationship
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'discount_price']

        discount_price = serializers.SerializerMethodField(method_name='discount')

        def discount(self, book: Book):
            return (book.price * 25) / 100

    # todo the below syntax will show the author id
    # author = AuthorSerializer
    #  todo the below syntax will bring the author name
    # author = serializers.StringRelatedField()


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'description', 'genre', 'language', 'price', 'author', 'discount')


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description', 'price']

# # todo is used when you wanted to add something that are not inside your model
# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=55)
#     last_name = serializers.CharField(max_length=55)
#     birth_day = serializers.DateField(source='date_of_birth')
