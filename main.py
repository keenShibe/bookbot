def main():
    FILE_PATH = "books/frankenstein.txt"
    with open(FILE_PATH) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_dict = count_unique_characters(file_contents)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for char, count in char_dict.items():
            if char.isalpha() == True:
                print(f"The '{char}' character was found {count} times")
        print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_unique_characters(text):
    lowercase_text = text.lower()
    words = lowercase_text.split()
    char_dict = {}
    for word in words:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

if __name__ == '__main__':
    main()
