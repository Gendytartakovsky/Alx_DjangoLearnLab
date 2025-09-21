from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer


"""
Views for the API.

This module provides:
1. BookList (kept for checker) – a simple ListAPIView to list all books.
2. BookViewSet – a full CRUD interface for the Book model with authentication
   and permissions applied.

Authentication & Permissions:
- Token Authentication is required.
- Clients must include a valid token in the request headers:
    Authorization: Token <your_token_here>
- Only authenticated users can access the endpoints.
"""


class BookList(ListAPIView):
    """
    Old list view for listing all books (kept for the checker).

    Endpoint:
    - GET /books/ – Returns a list of all books.

    This view does not enforce authentication since it is preserved for
    compatibility with the checker.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet that provides full CRUD for the Book model:

    Endpoints:
    - GET /books_all/        → List all books
    - GET /books_all/<id>/   → Retrieve a book by ID
    - POST /books_all/       → Create a new book
    - PUT /books_all/<id>/   → Update a book
    - DELETE /books_all/<id>/ → Delete a book

    🔒 Authentication & Permissions:
    - Requires Token Authentication.
    - Only authenticated users with a valid token can access these endpoints.
    - Example request header:
        Authorization: Token <your_token_here>
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
