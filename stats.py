def sort_on(dictionary):
    return dictionary["num"]

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
        c = c.lower()
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count

def sorted_char_count(char_count_dict: dict):
    # Sorts the character count dictionary by the number of occurrences
    # Descending order.
    
    sorted_char_count = []
    for c in char_count_dict:
        sorted_char_count.append({"name":c, "num": char_count_dict[c]})

    sorted_char_count.sort(key=sort_on, reverse=True)
    return sorted_char_count
