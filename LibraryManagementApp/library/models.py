from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#


class Books(models.Model):
    book_name = models.CharField(max_length=30)
    book_author = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.book_name

class LibraryTransaction(models.Model):
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_days = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.books

class LibraryUsers(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
