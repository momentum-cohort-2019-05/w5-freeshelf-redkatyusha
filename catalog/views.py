from django.shortcuts import render
from django.views import generic

# Create your views here.

from catalog.models import Book

def index(request):
    books = Book.objects.all()

    context = {
        "books": books,
    }

    return render(request, "index.html", context=context)

class BookListView(generic.ListView):
    model = Book