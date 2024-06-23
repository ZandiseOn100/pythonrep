books = {}

def add_book(book):
    books[book._name] = {"name": book._name, "author": book._author, "release_year": book._release_year}

def remove_book(name):
    if name in books:
        del books[name]

def search_book(name):
    if name in books:
        book = books[name]
        return f"'{book['name']}' by {book['author']} ({book['release_year']})"
    return "Book not found"

def list_books():
    return [f"'{book['name']}' by {book['author']} ({book['release_year']})" for book in books.values()]
