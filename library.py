import os

# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    @staticmethod
    def validate_title(title):
        if not title or not isinstance(title, str):
            raise ValueError("Invalid title provided.")
        return title

# Child class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return f"You have borrowed '{title}'."
        raise Exception(f"'{title}' is either unavailable or does not exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return f"'{title}' has been returned."
        raise Exception(f"'{title}' was not borrowed or does not exist.")

    def show_inventory(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(str(book) for book in self.books)

    @classmethod
    def load_data(cls):
        library = cls()
        if os.path.exists("library_data.txt"):
            with open("library_data.txt", "r") as file:
                for line in file:
                    title, author, is_borrowed = line.strip().split("|")
                    book = Book(title, author)
                    book.is_borrowed = is_borrowed == "True"
                    library.add_book(book)
        return library

    def save_data(self):
        with open("library_data.txt", "w") as file:
            for book in self.books:
                file.write(f"{book.title}|{book.author}|{book.is_borrowed}\n")
        print("Library data saved to library_data.txt.")


# Main program
def main():
    library = Library.load_data()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Show Inventory")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book = Book(Book.validate_title(title), author)
                library.add_book(book)
                print(f"Book '{title}' added successfully!")
            elif choice == 2:
                title = input("Enter the title of the book to borrow: ")
                print(library.borrow_book(title))
            elif choice == 3:
                title = input("Enter the title of the book to return: ")
                print(library.return_book(title))
            elif choice == 4:
                print("\nCurrent Inventory:")
                print(library.show_inventory())
            elif choice == 5:
                library.save_data()
                print("Library data saved. Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
