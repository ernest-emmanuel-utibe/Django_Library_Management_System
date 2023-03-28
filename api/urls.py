from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

urlpatterns = [
    # path('books/', views.BookListApiView.as_view(), name='book'),
    # path('book/<int:pk>/', views.BookDetailApiView.as_view(), name='detail'),
    path('', include(router.urls)),

    # todo author paths
    # path('authors/', views.AuthorListApiView.as_view()),
    # path('authors/<int:pk>/', views.BookDetailApiView.as_view(), name='detail'),
    # path('authors/<int:pk>/', views.AuthorDetailApiView.as_view()),
    # path('book-authors/', views.AuthorDetailApiView.as_view()),
    path('authors/<int:pk>/', views.author_detail, name='author-detail')

    # todo Below paths are for function based view
    # path('books/', views.book_List),
    # path('book/<int:pk>/', views.book_detail),
    # path('authors/', views.author_list),
    # path('author/<int:pk>/', views.author_detail)
]
