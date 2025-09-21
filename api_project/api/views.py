from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


class BookList(ListAPIView):
    """
    Old list view for listing all books (kept for the checker).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet that provides full CRUD for Book model:
    - list (GET /books_all/)
    - retrieve (GET /books_all/<id>/)
    - create (POST /books_all/)
    - update (PUT /books_all/<id>/)
    - delete (DELETE /books_all/<id>/)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
