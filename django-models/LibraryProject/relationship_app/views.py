from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# --- Function-Based View ---
def list_books(request):
    """
    List all books in the database
    """
    books = Book.objects.all()  # Query all books
    return render(request, "list_books.html", {"books": books})

# --- Class-Based View ---
class LibraryDetailView(DetailView):
    """
    Display details for a specific library, including all its books
    """
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
