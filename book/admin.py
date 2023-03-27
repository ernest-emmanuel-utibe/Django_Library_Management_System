from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
# admin.site.register(Genre)
admin.site.register(LibraryUser)
admin.site.register(BookInstance)
