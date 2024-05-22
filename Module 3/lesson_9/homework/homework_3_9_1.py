import random
import string


class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten_url(self, original_url):
        """Shortens the original URL and returns the shortened URL"""
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for i in range(6))
        self.urls[short_url] = original_url
        return "short.url/" + short_url

    def original_url(self, short_url):
        """Returns the original URL for the given shortened URL"""
        if short_url in self.urls:
            return self.urls[short_url]
        else:
            return None


def main():
    shortener = URLShortener()

    while True:
        print("Enter 1 to shorten a URL")
        print("Enter 2 to get the original URL")
        print("Enter 3 to exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            original_url = input("Enter the original URL: ")
            short_url = shortener.shorten_url(original_url)
            print("Shortened URL:", short_url)
        elif choice == "2":
            short_url = input("Enter the shortened URL: ")
            original_url = shortener.original_url(short_url)
            if original_url:
                print("Original URL:", original_url)
            else:
                print("URL not found")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
