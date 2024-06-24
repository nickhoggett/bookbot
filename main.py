def main():
    book_path = "books/Frankenstein.txt"
    book_text = read_file(book_path)
    words = word_count(book_text)
    get_chars = char_count(book_text)
    report(book_path, words, get_chars)

def report(path, words, get_chars):
    def char_report():
        report = ""
        for dict in get_chars:
            report += f"the {dict['char']} charecter was found {dict['num']}\n"
        return report
    print(f"---Begin report of {path}---\n {words} words found in the document\n\n {char_report()}")

def sort_on(list):
    return(list["num"])

def char_count(book_text):
    alphabet = {}
    for letter in book_text:
        letter = letter.lower()  # Converting the letter to lowercase
        if letter.isalpha(): # Only include letters of alphabet
            if letter in alphabet:
                alphabet[letter] += 1
            else:
                alphabet[letter] = 1
    alphabet_list = [{"char": k, "num": v} for k, v in alphabet.items()]
    alphabet_list.sort(reverse=True, key=sort_on)
    return(alphabet_list)

def read_file(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words = book.split()
    return(len(words))

main()
