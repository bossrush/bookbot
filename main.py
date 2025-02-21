from stats import get_num_words, get_character_count, get_sorted_list

def main():
    text_file = "books/frankenstein.txt"
    book_as_string = get_book_as_string(text_file)
    word_count = get_num_words(book_as_string)
    character_count = get_character_count(book_as_string)
    sorted_list = get_sorted_list(character_count)
    #print(book_as_string)
    #print(f"{word_count} words found in the document")
    #print(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_dict in sorted_list:
        character = list(character_dict.keys())[0]
        if character.isalpha():
            count = character_dict[character]
            print(f"{character}: {count}")
    print('============= END ===============')

def get_book_as_string(book_file):
    with open(book_file) as book:
        return book.read()


main()