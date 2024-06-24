def main():
    book_path = "books/Frankenstein.txt"
    book_text = read_file(book_path)
    words = word_count(book_text)
    print(words)

def read_file(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = book.split()
    return (len(words))

main()