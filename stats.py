def get_num_words(book):
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

def sort_on(dictionary):
    return list(dictionary.values())[0]

def get_sorted_list(dictionary):
    list_of_dictionaries = []
    for each_entry in dictionary:
        new_dict = {each_entry: dictionary[each_entry]}
        list_of_dictionaries.append(new_dict)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries