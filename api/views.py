from django.shortcuts import render, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from book.models import *
from .pagination import DefaultPageNumberPagination
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework import generics


# todo class base view


class AuthorViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListApiView(generics.ListAPIView, generics.CreateAPIView):
    # pagination_class = DefaultPageNumberPagination

    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


# class AuthorListApiView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetailApiView(generics.RetrieveDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
