from django.shortcuts import render
from rest_framework.response import Response
from book.models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics


# todo class base view
class BookListApiView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class AuthorListApiView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailApiView(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
