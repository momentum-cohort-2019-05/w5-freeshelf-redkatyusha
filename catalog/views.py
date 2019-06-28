from django.shortcuts import render

# Create your views here.

from catalog.models import Book

def index(request):
    books = Book.objects.all()

    context = {
        "books": books,
    }

    return render(request, "index.html", context=context)