import book_module
from book import Book

def main():
    while True:
        print("\n1. Add a book with title, author, and publication year.")
        print("2. Remove a book by title.")
        print("3. Search for a book by title.")
        print("4. List all books.")
        print("5. Quit")
        
        choice = int(input("Select an operation: "))
        
        if choice == 1:
            name = input("Enter book name: ")
            author = input("Enter book author: ")
            release_year = input("Enter publication year: ")
            book = Book(name, author, release_year)
            book_module.add_book(book)
        elif choice == 2:
            name = input("Enter book name to remove: ")
            book_module.remove_book(name)
        elif choice == 3:
            name = input("Enter book name to search: ")
            result = book_module.search_book(name)
            print(result)
        elif choice == 4:
            book_list = book_module.list_books()
            for book in book_list:
                print(book)
        elif choice == 5:
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()
