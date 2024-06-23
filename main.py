def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        return print(file_contents)

main()