class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.checked_out = False

    def __str__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"{self.title} by {self.author} ({self.num_pages} pages) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book '{title}' was not found.")

    def check_out(self, title):
        book = self.find_book(title)

        if book is None:
            print(f"Book '{title}' was not found.")
        elif book.checked_out:
            print(f"Book '{book.title}' is already checked out.")
        else:
            book.checked_out = True
            print(f"Book '{book.title}' has been checked out.")

    def check_in(self, title):
        book = self.find_book(title)

        if book is None:
            print(f"Book '{title}' was not found.")
        elif not book.checked_out:
            print(f"Book '{book.title}' is already available.")
        else:
            book.checked_out = False
            print(f"Book '{book.title}' has been returned.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def print_books(self):
        print("\nBooks currently in library:")
        for book in self.books:
            print(book)


def main():
    library = Library()

    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    book3 = Book("The Hobbit", "J.R.R. Tolkien", 310)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.check_out("1984")
    library.check_in("1984")
    library.remove_book("The Hobbit")

    library.print_books()


if __name__ == "__main__":
    main()
