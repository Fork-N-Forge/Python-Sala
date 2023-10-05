import random
import string

class URLShortener:
    def __init__(self):
        self.url_database = {}
        self.short_code_length = 6  # You can adjust the length as needed

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.short_code_length))

    def shorten_url(self, long_url):
        if long_url in self.url_database:
            return self.url_database[long_url]
        else:
            short_code = self.generate_short_code()
            self.url_database[long_url] = short_code
            return short_code

    def expand_url(self, short_code):
        for long_url, code in self.url_database.items():
            if code == short_code:
                return long_url
        return None

def main():
    url_shortener = URLShortener()

    while True:
        print("\nOptions:")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            long_url = input("Enter the URL to shorten: ")
            short_code = url_shortener.shorten_url(long_url)
            print(f"Shortened URL: http://your-short-url.com/{short_code}")
        elif choice == '2':
            short_code = input("Enter the short code to expand: ")
            long_url = url_shortener.expand_url(short_code)
            if long_url:
                print(f"Expanded URL: {long_url}")
            else:
                print("Short code not found.")
        elif choice == '3':
            print("Exiting URL Shortener.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
