def count_words(text):
    count = len(text.split())
    print(f'Found {count} total words')

def count_letters(text):
    letter_count_dict = dict()
    
    for char in text.lower():
        if char in letter_count_dict:
            letter_count_dict[char] += 1
        else:
            letter_count_dict[char] = 1

    return letter_count_dict


def order_dict(dictionary):
    # We have to iterate through the dictionary and at each key, create a new dictionary
    # where that dictionary contains the required values
    # EX: {'char': 'a', 'count': 7}
    cleaned_list = [] 

    for key in dictionary:
        if key.isalpha():
            temp_dict = dict()
        
            temp_dict['char'] = key
            temp_dict['count'] = dictionary[key]
        
            cleaned_list.append(temp_dict)  
    cleaned_list.sort(reverse=True, key=sort_key)
    return cleaned_list

def sort_key(dictionary):
    return dictionary['count']
