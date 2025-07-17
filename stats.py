def book_word_count(book_text: str):
    # Takes a string containing the text of a book 
    # and returns the number of words in it.
    split_text = book_text.split()
    return len(split_text)

def book_char_count(book_text: str):
    # Takes a string containing the text of a book 
    # and counts the occurances of each character
    char_count = {}
    for c in book_text:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count
