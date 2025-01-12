def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"There are {num_words} words in this document.")
    num_char = char_count(text)
    print(num_char)

def get_book_text(path):
      with open(path) as f:
        return f.read()
      
def word_count(input):
    words = input.split()
    return len(words)
    
def char_count(input):
    lower_text = input.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


main()