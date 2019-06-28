from django.shortcuts import render
from django.views import generic

# Create your views here.

from catalog.models import Book, Category

def index(request):
    recent_books = Book.objects.all().order_by('-created')[0: 5]

    context = {
        "recent_books": recent_books,
    }

    return render(request, "index.html", context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 20

class BookDetailView(generic.DetailView):
    model = Book

class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 20

class CategoryDetailView(generic.DetailView):
    model = Category