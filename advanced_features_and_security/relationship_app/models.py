from django.db import models
from django.conf import settings

# ------------------------------
# Author Model
# ------------------------------
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ------------------------------
# Book Model
# ------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# ------------------------------
# Library Model
# ------------------------------
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # links to CustomUser
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_libraries'
    )

    def __str__(self):
        return self.name


# ------------------------------
# Librarian Model
# ------------------------------
class Librarian(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # links to CustomUser
        on_delete=models.CASCADE
    )
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
