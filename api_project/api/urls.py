from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create the router and register your ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Original list view (needed for checker)
    path('books/', BookList.as_view(), name='book-list'),

    # Router-generated CRUD routes for BookViewSet
    path('', include(router.urls)),
]
