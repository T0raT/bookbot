import stats # never really cared but import this way to not have functions fully take over the namespace
# This is a little more verbose than "from stats import *"
# Wether this is industry standard or not, idk.
import sys

def get_book_text(book_path: str):
    # Takes a path to a book file and returns its content as a string.
    with open(book_path, 'r', encoding='utf-8') as book:
        return book.read()


def main():
    arguments = sys.argv # Recieve user CLI arguments
    if len(arguments) != 2:
        # Not 2 arguments, exit program with status code 1
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = arguments[1] # 2nd argument is the path to the book file
    
    book_text = get_book_text(path)
    word_count = stats.book_word_count(book_text)
    char_count = stats.book_char_count(book_text)
    sorted_char_count = stats.sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for i in sorted_char_count:
        print(f"{i['name']}: {i['num']}")

    print("============= END ===============")
    return None

if __name__ == "__main__":
    main()
