def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower_letters = text.lower()
    letters = get_num_letters(lower_letters)
    organized_letters = organize(letters)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for item in organized_letters:
        print(f"The {item["character"]} character was found {item["num"]} times")
    print(f"--- End report ---")

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
    return letters

def organize(letters):
    sorted = []
    for let in letters:
        sorted.append({"character": let, "num": letters[let]})
    sorted.sort(reverse=True, key=sort_on)
    print(sorted)
    return sorted

def get_book_text(path):
    with open(path) as f:
        return f.read()
def sort_on(dict_item):
    return dict_item["num"]

main()
