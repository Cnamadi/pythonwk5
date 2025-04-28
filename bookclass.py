class Book:
    def __init__(self, title, author, genre, year):
        """Constructor to initialize book attributes"""
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def get_description(self):
        """Returns a description of the book"""
        return f"'{self.title}' by {self.author}, published in {self.year}. Genre: {self.genre}."

    def is_classic(self):
        """Checks if the book is a classic (published before 1950)"""
        return self.year < 1950


# Inheritance: FictionBook inherits from Book
class FictionBook(Book):
    def __init__(self, title, author, year, subgenre):
        """Constructor to initialize fiction book attributes"""
        super().__init__(title, author, "Fiction", year)
        self.subgenre = subgenre

    def get_description(self):
        """Overrides the parent method to include subgenre"""
        return f"'{self.title}' by {self.author}, published in {self.year}. Subgenre: {self.subgenre}."


