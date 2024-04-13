class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, author, title):
        if author in self.books:
            self.books[author].append(title)
        else:
            self.books[author] = [title]

    def display_by_author(self):
        sorted_books = sorted(self.books.items(), key=lambda x: x[0])
        for author, titles in sorted_books:
            print(f"Author: {author}")
            for title in titles:
                print(f"- {title}")
            print()

    def display_by_title(self):
        all_titles = []
        for titles in self.books.values():
            all_titles.extend(titles)
        sorted_titles = sorted(all_titles)
        for title in sorted_titles:
            print(title)


def main():
    library = Library()

    library.add_book("Stephen King", "The Shining")
    library.add_book("Stephen King", "It")
    library.add_book("J.K. Rowling", "Harry Potter and the Philosopher's Stone")
    library.add_book("J.K. Rowling", "Harry Potter and the Chamber of Secrets")
    library.add_book("Leo Tolstoy", "War and Peace")

    print("Books sorted by author:")
    library.display_by_author()

    print("\nBooks sorted by title:")
    library.display_by_title()


if __name__ == "__main__":
    main()
