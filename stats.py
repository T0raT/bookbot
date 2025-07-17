def book_word_count(book_text: str):
    # Takes a string containing the text of a book 
    # and returns the number of words in it.
    split_text = book_text.split()
    return len(split_text)
