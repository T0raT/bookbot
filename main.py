from stats import book_word_count

def get_book_text(book_path: str):
    # Takes a path to a book file and returns its content as a string.
    with open(book_path, 'r', encoding='utf-8') as book:
        return book.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = book_word_count(book_text)
    print(f"{word_count} words found in the document")
    return None

if __name__ == "__main__":
    main()
