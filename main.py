def main():
    text_file = "books/frankenstein.txt"
    book_as_string = get_book_as_string(text_file)
    word_count = get_word_count(book_as_string)
    character_count = get_character_count(book_as_string)
    #print(book_as_string)
    #print(word_count)
    #print(character_count)



def get_book_as_string(book_file):
    with open(book_file) as book:
        return book.read()
        
def get_word_count(book):
    return len(book.split())

def get_character_count(book):
    lower_case_string = book.lower()
    #character_set = list(lower_case_string)
    character_dict = {}
    for each_character in lower_case_string:
        if each_character not in character_dict:
            character_dict[each_character] = 1
        else:
            character_dict[each_character] += 1
    return character_dict

#def get_bookbot_report():



main()