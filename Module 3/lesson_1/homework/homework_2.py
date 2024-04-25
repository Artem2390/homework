class BookReview:
    def __init__(self, book, review_text):
        self.book = book
        self.review_text = review_text


class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review_text):
        review = BookReview(self, review_text)
        self.reviews.append(review)

    def __repr__(self):
        return f"Book(author={self.author}, title={self.title}, year={self.year}, genre={self.genre})"

    def __str__(self):
        review_texts = "\n".join([review.review_text for review in self.reviews])
        return f"{self.title} by {self.author} ({self.year}) - {self.genre}\nReviews:\n{review_texts}"


book1 = Book("George Orwell", "1984", 1949, "Dystopian fiction")
book1.add_review("Great book, highly recommended!")
book1.add_review("A classic that everyone should read.")

book2 = Book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", 1997, "Fantasy")
book2.add_review("Magical adventure for all ages.")

print(book1)
print(book2)
