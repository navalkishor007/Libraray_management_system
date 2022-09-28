from django.shortcuts import render
from .models import LibraryUsers, LibraryTransaction, Books
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


@login_required
def home(request):
    data = Books.objects.all()
    user = request.user
    return render(request, 'library/home.html', {'data': data, 'name': user})

def borrow_book(request, id):
    book_obj = Books.objects.get(id=id)
    form = LibraryTransaction()
    if request.method == 'POST':
        if book_obj.quantity > 0:
            book_obj.quantity -= 1
    return render(request, form)


@staff_member_required
def book_transaction(request):
    data = LibraryTransaction.objects.all()
    return render(request, 'library/book_transaction.html', {'trans': data})
