# class_genre.py

class Genre:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._categories = []  # Initialize _categories as an empty list
    
    def add_category(self, category):
        if category not in self._categories:
            self._categories.append(category)
        else:
            print(f"Category '{category}' already exists in genre '{self._name}'.")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_categories(self):
        return self._categories

    def set_categories(self, categories):
        self._categories = categories

