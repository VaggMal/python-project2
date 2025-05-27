# Κλάση για την αναπαράσταση ενός βιβλίου
class Book:
    def __init__(self, isbn, title, author, year):
        # Μοναδικός κωδικός βιβλίου
        self.isbn = isbn
        # Τίτλος βιβλίου
        self.title = title
        # Συγγραφέας
        self.author = author
        # Έτος έκδοσης
        self.year = year
        # Διαθεσιμότητα βιβλίου (True=διαθέσιμο)
        self.available = True
        # Ποιος έχει δανειστεί το βιβλίο (αν υπάρχει)
        self.borrower = None

    def __str__(self):
        # Επιστρέφει αναγνωρίσιμη περιγραφή του βιβλίου
        status = "Διαθέσιμο" if self.available else f"Δανεισμένο σε: {self.borrower.name}"
        return f'[{self.isbn}] "{self.title}" του {self.author} ({self.year}) - {status}'

    def __repr__(self):
        return self.__str__()

# Κλάση για τα μέλη της βιβλιοθήκης
class Member:
    def __init__(self, member_id, name, email):
        # Μοναδικό ID μέλους
        self.member_id = member_id
        # Όνομα μέλους
        self.name = name
        # Email μέλους
        self.email = email
        # Λίστα με τα βιβλία που έχει δανειστεί το μέλος
        self.borrowed_books = []

    def borrow_book(self, book):
        # Δανεισμός βιβλίου αν είναι διαθέσιμο
        if book.available:
            book.available = False
            book.borrower = self
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        # Επιστροφή βιβλίου αν το έχει δανειστεί το μέλος
        if book in self.borrowed_books:
            book.available = True
            book.borrower = None
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        # Επιστρέφει περιγραφή μέλους
        return f'{self.member_id}: {self.name} ({self.email})'

    def __repr__(self):
        return self.__str__()

# Κλάση βιβλιοθηκάριου (κληρονομεί από Member)
class Librarian(Member):
    def can_manage_library(self):
        # Ο βιβλιοθηκάριος μπορεί να διαχειριστεί τη βιβλιοθήκη
        return True

# Κλάση για τη βιβλιοθήκη
class Library:
    def __init__(self):
        # Λεξικό με τα βιβλία της βιβλιοθήκης (κλειδί: isbn, τιμή: Book)
        self.books = {}
        # Λεξικό με τα μέλη της βιβλιοθήκης (κλειδί: member_id, τιμή: Member)
        self.members = {}
        # Ιστορικό δανεισμών/επιστροφών βιβλίων
        self.history = []  # list of (action, member, book)

    def add_book(self, book):
        # Προσθήκη βιβλίου στη βιβλιοθήκη
        self.books[book.isbn] = book

    def remove_book(self, isbn):
        # Αφαίρεση βιβλίου από τη βιβλιοθήκη αν είναι διαθέσιμο
        if isbn in self.books and self.books[isbn].available:
            del self.books[isbn]
            return True
        return False

    def register_member(self, member):
        # Εγγραφή μέλους στη βιβλιοθήκη
        self.members[member.member_id] = member

    def remove_member(self, member_id):
        # Αφαίρεση μέλους από τη βιβλιοθήκη αν δεν έχει δανειστεί βιβλία
        member = self.members.get(member_id)
        if member and not member.borrowed_books:
            del self.members[member_id]
            return True
        return False

    def borrow_book(self, member_id, isbn):
        # Δανεισμός βιβλίου σε μέλος
        member = self.members.get(member_id)
        book = self.books.get(isbn)
        if member and book and book.available:
            if member.borrow_book(book):
                self.history.append(("borrow", member, book))
                return True
        return False

    def return_book(self, member_id, isbn):
        # Επιστροφή δανεισμένου βιβλίου από μέλος
        member = self.members.get(member_id)
        book = self.books.get(isbn)
        if member and book and book in member.borrowed_books:
            if member.return_book(book):
                self.history.append(("return", member, book))
                return True
        return False

    def search_books(self, by="title", keyword=""):
        # Αναζήτηση βιβλίων με βάση διάφορα κριτήρια (π.χ. τίτλος, συγγραφέας)
        result = []
        for book in self.books.values():
            if keyword.lower() in getattr(book, by).lower():
                result.append(book)
        return result

    def show_borrowed_books(self):
        # Εμφάνιση όλων των δανεισμένων βιβλίων
        return [book for book in self.books.values() if not book.available]

    def show_history(self):
        # Εμφάνιση ιστορικού δανεισμών και επιστροφών
        for action, member, book in self.history:
            print(f"{action.title()}: {member.name} -> {book.title}")


if __name__ == "__main__":
    library = Library()

    # Προσθήκη βιβλίων
    b1 = Book("001", "Οδύσσεια", "Όμηρος", 800)
    b2 = Book("002", "Η Ιλιάδα", "Όμηρος", 750)
    library.add_book(b1)
    library.add_book(b2)

    # Προσθήκη μελών
    m1 = Member("m01", "Γιάννης Παπαδόπουλος", "giannis@email.com")
    m2 = Librarian("m02", "Μαρία Βιβλιοθηκάριος", "maria@email.com")
    library.register_member(m1)
    library.register_member(m2)

    # Δανεισμός βιβλίου
    print("\nΔανεισμός βιβλίου:")
    library.borrow_book("m01", "001")
    for book in m1.borrowed_books:
        print(book)

    # Επιστροφή βιβλίου
    print("\nΕπιστροφή βιβλίου:")
    library.return_book("m01", "001")
    print("Επιστράφηκαν όλα τα βιβλία;" , len(m1.borrowed_books) == 0)

    # Διαγραφή μέλους (επιτυχής)
    print("\nΔιαγραφή μέλους:")
    print("Διαγράφηκε;", library.remove_member("m01"))

    # Αναζήτηση βιβλίων με φίλτρο τίτλου
    print("\nΑναζήτηση για 'Η':")
    for book in library.search_books(by="title", keyword="Η"):
        print(book)

    # Προβολή δανεισμένων βιβλίων
    print("\nΔανεισμένα βιβλία:")
    for book in library.show_borrowed_books():
        print(book)

    # Προβολή ιστορικού
    print("\nΙστορικό κινήσεων:")
    library.show_history()

