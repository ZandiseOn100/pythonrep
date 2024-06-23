class Book:
    def __init__(self, name, author, release_year):
        self._name = name
        self._author = author
        self._release_year = release_year
    
    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author
    
    def get_release_year(self):
        return self._release_year
    
    def set_release_year(self, release_year):
        self._release_year = release_year

    def __str__(self):
        return f"'{self._name}' by {self._author} ({self._release_year})"
