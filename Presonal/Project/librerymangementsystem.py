class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nList of Books in the Library:")
            for book in self.books:
                status = "Available" if book.available else "Not Available"
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")
    
    def display_members(self):
        if not self.members:
            print("No members are registered in the library.")
        else:
            print("\nList of Members:")
            for member in self.members:
                borrowed_books = ", ".join([book.title for book in member.borrowed_books]) or "No books borrowed"
                print(f"Name: {member.name}, Member ID: {member.member_id}, Borrowed Books: {borrowed_books}")


def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Show members")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print(f"Book '{title}' added to the library.")

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.add_member(member)
            print(f"Member '{name}' added to the library.")

        elif choice == "3":
            member_id = input("Enter member ID: ")
            title = input("Enter book title to borrow: ")
            member = library.find_member(member_id)
            book = library.find_book(title)
            if member and book:
                if member.borrow_book(book):
                    print(f"Book '{title}' borrowed by {member.name}.")
                else:
                    print(f"Book '{title}' is not available.")
            else:
                print("Invalid member ID or book title.")

        elif choice == "4":
            member_id = input("Enter member ID: ")
            title = input("Enter book title to return: ")
            member = library.find_member(member_id)
            book = library.find_book(title)
            if member and book:
                if member.return_book(book):
                    print(f"Book '{title}' returned by {member.name}.")
                else:
                    print(f"{member.name} has not borrowed '{title}'.")
            else:
                print("Invalid member ID or book title.")

        elif choice == "5":
            library.display_books()
        
        elif choice == "6":
            library.display_members()

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



main()
