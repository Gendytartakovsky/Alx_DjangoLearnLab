import os
import sys
import django

# --- Add project root to Python path ---
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# --- Setup Django ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- SAMPLE DATA CREATION ---
def create_sample_data():
    # Create author if not exists
    author, _ = Author.objects.get_or_create(name="George Orwell")
    
    # Create books if not exists
    book1, _ = Book.objects.get_or_create(title="1984", author=author)
    book2, _ = Book.objects.get_or_create(title="Animal Farm", author=author)

    # Create library if not exists
    library, _ = Library.objects.get_or_create(name="Central Library")
    library.books.set([book1, book2])  # assign books to library

    # Create librarian if not exists
    Librarian.objects.get_or_create(name="Alice", library=library)

# --- QUERIES ---
def run_queries():
    # 1. Query all books by a specific author
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:", [book.title for book in books])

    # 2. List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(f"Books in {library_name}:", [book.title for book in library.books.all()])

    # 3. Retrieve the librarian for a library
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian of {library_name}:", librarian.name)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    create_sample_data()  # ensures data exists
    run_queries()
