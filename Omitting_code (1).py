def omtting_vowels(word):
    vowels="aeiouAEIOU"
    omit=""
    for char in word:
        if char not in vowels:
            omit+="".join(char)
    return omit
word=input("\nEnter the word: ")
print(f"Word without vowels is: {omtting_vowels(word)}")
print("\n")
            