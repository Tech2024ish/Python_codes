def strings_to_len(strings):
    my_dict = {}
    
    for string in strings:
        my_dict[string] = len(string)
    
    return my_dict


strings =  ["apple", "banana", "Tiger"]
print (strings_to_len(strings))

