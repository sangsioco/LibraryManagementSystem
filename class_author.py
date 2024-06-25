class Author:
    def __init__(self, first_name, last_name, biography):
        self._first_name = first_name
        self._last_name = last_name
        self._biography = biography

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name
    
    def get_name(self):
        return f"{self._first_name} {self._last_name}"

    def set_name(self, name):
        self._name = name

    def get_biography(self):
        return self._biography

    def set_biography(self, biography):
        self._biography = biography



