def main():
    book_path = "books/Frankenstein.txt"
    book_text = read_file(book_path)
    words = word_count(book_text)
    char_count(book_text)

def char_count(book_text):
    alphabet = {}
    for letter in book_text:
        letter = letter.lower()  # Converting the letter to lowercase
        if letter in alphabet:
            alphabet[letter] += 1
        else:
            alphabet[letter] = 1
    print(alphabet)

# expected outcome
# {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504, 'e': 46043, 'c': 9243, 't': 30365, ' ': 74144, 'g': 5974, 'u': 10407, 'n': 24367, 'b': 5026, "'": 229, 's': 21155, 'f': 8731, 'a': 26743, 'k': 1755, 'i': 24613, ',': 5097, 'y': 7914, 'm': 10604, 'w': 7638, 'l': 12739, '(': 39, 'd': 16863, ')': 39, 'h': 19725, '\n': 7651, 'v': 3833, '.': 3124, '-': 445, ':': 68, '1': 92, '7': 23, '2': 24, '0': 21, '8': 20, '[': 4, '#': 1, '4': 17, ']': 4, '*': 28, 'z': 243, '?': 220, ';': 970, 'x': 677, 'q': 324, '!': 239, '"': 796, '3': 18, '5': 16, '9': 13, '6': 10, '_': 2, '/': 24, '%': 1, '@': 2, '$': 2}

def read_file(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = book.split()
    return(len(words))


main()
