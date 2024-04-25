class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return f"Book(author={self.author}, title={self.title}, year={self.year}, genre={self.genre})"

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.genre}"


book1 = Book("George Orwell", "1984", 1949, "Dystopian fiction")
book2 = Book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", 1997, "Fantasy")
book3 = Book("Harper Lee", "To Kill a Mockingbird", 1960, "Fiction")

print(repr(book1))
print(str(book2))
print(book3)
