class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def display_info(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f'Book Title  : {self.title}')
        print(f'Book Author : {self.author}')
        print(f'Book Status : {status}')


class Library:
    def __init__(self):
        self.books = []

    # Add new book
    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'New book "{title}" added successfully.')

    # View all books
    def view_books(self):
        if not self.books:
            print('No books available in the library.')
        else:
            print('\n--- Library Catalog ---')
            for book in self.books:
                book.display_info()
                print()

    # Borrow a book
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f'Book "{book.title}" has been borrowed. Enjoy reading!')
                return

        print(f'Book "{title}" is not available for borrowing.')

    # Return a book
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f'Book "{book.title}" has been returned.')
                return

        print(f'Book "{title}" is not currently borrowed or does not exist.')

    # Search for a book
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display_info()
                return

        print(f'Book "{title}" is not available in the library.')


# Main program
library = Library()

while True:
    print('\nLibrary Management System')
    print('1. Add Book')
    print('2. View All Books')
    print('3. Borrow Book')
    print('4. Return Book')
    print('5. Search Book')
    print('6. Exit')

    try:
        choice = int(input('Enter your choice (1-6): '))
        
        if choice == 1:
            title = input('Enter book title: ').strip()
            author = input('Enter book author: ').strip()
            library.add_book(title, author)

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            title = input('Enter book title: ').strip()
            library.borrow_book(title)

        elif choice == 4:
            title = input('Enter book title: ').strip()
            library.return_book(title)

        elif choice == 5:
            title = input('Enter book title: ').strip()
            library.search_book(title)

        elif choice == 6:
            print('Thank you for visiting the library!')
            break

        else:
            print("Invalid choice. Please pick between 1–6.")

    except Exception as e:
        print("Error:", e)
