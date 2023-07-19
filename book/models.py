from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related


# Create your models here.

class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'FIC'),
        ('COMEDY', 'COM'),
        ('ROMANCE', 'ROM'),
        ('DEVELOPER', 'DEV'),
        ('FINANCE', 'FIN'),
        ('ADVENTURE', 'ADV'),
        ('DRAMA', 'DRA'),
        ('FANTASY', 'FAN'),
        ('THRILLER', 'THR'),
        ('BIOGRAPHY', 'BIO'),
    ]

    LANGUAGE_CHOICES = [
        ('ENGLISH', 'ENG'),
        ('FRENCH', 'FRE'),
        ('SPANISH', 'SPN'),
        ('YORUBA', 'YOR'),
        ('IGBO', 'IGB'),
        ('HAUSA', 'HAU')
    ]

    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=15, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=20, default="")
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, default="")
    price = models.DecimalField(default=0, max_digits=6, decimal_places=3)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    STATUS_CHOICE = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    imprint = models.CharField(max_length=55, blank=False, null=False)

    def __str__(self):
        return self.imprint
