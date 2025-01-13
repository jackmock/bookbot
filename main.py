def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text)
    char_report(book_path, num_words, num_char)

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

def char_report(path, wordcount, input):
    alpha_only = {}
    for char in input:
        if char.isalpha():
            alpha_only[char] = input[char]
    alpha_only_sorted = sorted(alpha_only.items(), key=lambda item: item[1], reverse=True)

    
    print(f"--- Begin report of {path} ---")
    print(f"There are {wordcount} words in this document \n")
    for char, count in alpha_only_sorted:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()