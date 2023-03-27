from django.urls import path
from api import views

urlpatterns = [
    path('book/', views.BookListApiView.as_view(), name='book'),
    path('book/<int:pk>/', views.BookDetailApiView.as_view(), name='detail'),
    # todo author paths
    path('authors/', views.AuthorListApiView.as_view()),
    path('authors/<int:pk>/', views.AuthorDetailApiView.as_view(), name='detail'),

    # todo Below paths are for function based view
    # path('books/', views.book_List),
    # path('book/<int:pk>/', views.book_detail),
    # path('authors/', views.author_list),
    # path('author/<int:pk>/', views.author_detail)
]
