def main():
    title = "books/frankenstein.txt"
    with open(title) as f:
        file_contents = f.read()
        words = file_contents.split()
    print(f"--- Begin report of {title} ---")
        
    # Read Book function (currently unused)
    def read_text():
        print(file_contents)

    # Count total words function
    def word_count():
        print(f"{len(words)} words found in the document")
    word_count()

    # Convert text to lowercase function + create new list of converted characters
    def lower_convert():
        lower_text = file_contents.lower()
        lower_char = list(lower_text)
            
        # Letter frequency function
        def letter_count(lower_char):
            dictionary = {
                "a": 0,
                "b": 0,
                "c": 0,
                "d": 0,
                "e": 0,
                "f": 0,
                "g": 0,
                "h": 0,
                "i": 0,
                "j": 0,
                "k": 0,
                "l": 0,
                "m": 0,
                "n": 0,
                "o": 0,
                "p": 0,
                "q": 0,
                "r": 0,
                "s": 0,
                "t": 0,
                "u": 0,
                "v": 0,
                "w": 0,
                "x": 0,
                "y": 0,
                "z": 0
                }
            # Convert to characters & print the frequency
            for letter in lower_char:
                if letter in dictionary:
                    dictionary[letter] += 1
            for key, count in dictionary.items():
                print(f"The {key} character was found {count} times")
        letter_count(lower_char)      
    lower_convert()  
    print("--- End report ---")                     
main()
