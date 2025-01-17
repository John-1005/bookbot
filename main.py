def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower_letters = text.lower()
    letters = get_num_letters(lower_letters)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(lower_letters):
    letters = {}
    for char in lower_letters:
        if char.isalpha():
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
    print(letters)
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
