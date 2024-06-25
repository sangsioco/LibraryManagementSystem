class User:
    def __init__(self, first_name, last_name, library_id):
        self._first_name = first_name
        self._last_name = last_name
        self._library_id = library_id
        self._borrowed_books = []
        self._reserved_books = []

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name
    
    def get_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_library_id(self):
        return self._library_id

    def borrow_book(self, book):
        if book.borrow_book(self):
            self._borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book)
            return True
        return False

    def reserve_book(self, book):
        if book.reserve_book(self):
            self._reserved_books.append(book)
            return True
        return False

    def cancel_reservation(self, book):
        if book in self._reserved_books:
            book.cancel_reservation()
            self._reserved_books.remove(book)
            return True
        return False

    def get_borrowed_books(self):
        return [book.get_ISBN() for book in self._borrowed_books]

    def get_reserved_books(self):
        return [book.get_ISBN() for book in self._reserved_books]
