
---

### **2️⃣ retrieve.md**
```markdown
# Retrieve Operation

```python
# Retrieve the book we just created
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.title, retrieved_book.author, retrieved_book.publication_year

('1984', 'George Orwell', 1949)
