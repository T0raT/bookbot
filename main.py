import stats # never really cared but import this way to not have functions fully take over the namespace
# This is a little more verbose than "from stats import *"
# Wether this is industry standard or not, idk.

def get_book_text(book_path: str):
    # Takes a path to a book file and returns its content as a string.
    with open(book_path, 'r', encoding='utf-8') as book:
        return book.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = stats.book_word_count(book_text)
    char_count = stats.book_char_count(book_text)
    print(f"{word_count} words found in the document")
    print(char_count)
    return None

if __name__ == "__main__":
    main()
