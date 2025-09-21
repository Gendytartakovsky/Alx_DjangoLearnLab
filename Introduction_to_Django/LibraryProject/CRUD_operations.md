# CRUD Operations for Book Model

## Create
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

<Book: 1984 by George Orwell (1949)>

# Retrieve the book we just created
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.title, retrieved_book.author, retrieved_book.publication_year

('1984', 'George Orwell', 1949)

# Update the title of the book
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book.title

'Nineteen Eighty-Four'

# Delete the book
retrieved_book.delete()
Book.objects.all()

(<number of deleted objects>, {'bookshelf.Book': 1})
<QuerySet []>

