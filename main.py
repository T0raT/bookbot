def get_book_text(book_path: str):
    # Takes a path to a book file and returns its content as a string.
    with open(book_path, 'r', encoding='utf-8') as book:
        return book.read()


def main():
    print(get_book_text("books/frankenstein.txt"))


if __name__ == "__main__":
    main()
