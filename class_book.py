class Book:
    def __init__(self, title, author, ISBN, publication_date, genre_name, category):
        self._title = title
        self._author = author
        self._ISBN = ISBN
        self._publication_date = publication_date
        self._genre_name = genre_name
        self._category = category
        self._borrowed = False
        self._reserved_by = None

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_ISBN(self):
        return self._ISBN

    def is_available(self):
        return not self._borrowed and not self._reserved_by

    def borrow_book(self, user):
        if self.is_available():
            self._borrowed = True
            self._reserved_by = None
            return True
        return False

    def return_book(self):
        self._borrowed = False

    def reserve_book(self, user):
        if self.is_available():
            self._reserved_by = user
            return True
        return False

    def cancel_reservation(self):
        self._reserved_by = None

    def get_reserved_by(self):
        return self._reserved_by
