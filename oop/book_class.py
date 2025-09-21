# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize the Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a human-readable string."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a string to recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
