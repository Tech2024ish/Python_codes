def word_frequencies(sequence):
    if isinstance(sequence, str):
        words = sequence.split()
    else:
        words = sequence  
    
    frequency_dict = {}
    
    for word in words:
        word = word.lower()
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    
    return frequency_dict
sequence = "apple banana apple cherry banana"
result = word_frequencies(sequence)
print(result)  
