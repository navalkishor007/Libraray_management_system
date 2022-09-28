from django.contrib import admin
from .models import Books, LibraryTransaction
# Register your models here.



admin.site.register(Books)
admin.site.register(LibraryTransaction)