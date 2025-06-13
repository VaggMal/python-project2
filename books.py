# library_system.py

# Κλάση που αναπαριστά ένα βιβλίο στη βιβλιοθήκη
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.available = True
        self.borrower = None

    def __str__(self):
        return f'{self.title} by {self.author} ({self.year}) [{self.isbn}]'

    def __repr__(self):
        return self.__str__()

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        # Λίστα με τα βιβλία που έχει δανειστεί το μέλος
        self.borrowed_books = []

    # Συνάρτηση για δανεισμό βιβλίου από το μέλος
    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            book.borrower = self
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available.")

    # Συνάρτηση για επιστροφή βιβλίου από το μέλος
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            book.borrower = None
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} doesn't have {book.title}")

    def __str__(self):
        return f"{self.name} ({self.member_id})"

    def __repr__(self):
        return self.__str__()

class Librarian(Member):
    def can_manage_library(self):
        return True

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # Συνάρτηση για προσθήκη βιβλίου στη βιβλιοθήκη
    def add_book(self, book):
        self.books[book.isbn] = book

    # Συνάρτηση για αφαίρεση βιβλίου από τη βιβλιοθήκη
    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    # Συνάρτηση για εγγραφή μέλους στη βιβλιοθήκη
    def register_member(self, member):
        self.members[member.member_id] = member

    # Συνάρτηση για αφαίρεση μέλους από τη βιβλιοθήκη
    def remove_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]

    # Συνάρτηση για δανεισμό βιβλίου σε μέλος
    def borrow_book(self, member_id, isbn):
        if member_id in self.members and isbn in self.books:
            member = self.members[member_id]
            book = self.books[isbn]
            member.borrow_book(book)

    # Συνάρτηση για επιστροφή βιβλίου από μέλος
    def return_book(self, member_id, isbn):
        if member_id in self.members and isbn in self.books:
            member = self.members[member_id]
            book = self.books[isbn]
            member.return_book(book)

    # Συνάρτηση για αναζήτηση βιβλίων στη βιβλιοθήκη
    def search_books(self, by="title", keyword=""):
        result = []
        for book in self.books.values():
            if keyword.lower() in getattr(book, by).lower():
                result.append(book)
        return result

    # Συνάρτηση για εμφάνιση δανεισμένων βιβλίων
    def show_borrowed_books(self):
        return [book for book in self.books.values() if not book.available]

# Παράδειγμα Χρήσης
if __name__ == "__main__":
    lib = Library()

    b1 = Book("001", "Python", "k.Dadaliaris", 2000)
    b2 = Book("002", "Maths", "Malissovas", 2004)
    lib.add_book(b1)
    lib.add_book(b2)

    m1 = Member("M001", "Vaggelis", "vagg@gmail.com")
    m2 = Librarian("M002", "Dada", "dada@gmail.com")
    lib.register_member(m1)
    lib.register_member(m2)

    lib.borrow_book("M001", "001")
    lib.borrow_book("M001", "002")
    lib.return_book("M001", "001")

    print("\n Αναζήτηση:")
    for book in lib.search_books(by="title", keyword="Math"):
        print(book)

    print("\n Δανεισμένα Βιβλία:")
    for book in lib.show_borrowed_books():
        print(book)


