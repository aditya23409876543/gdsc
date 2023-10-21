def length_of_last_word(s):
    # Split the string by spaces
    words = s.split()
    
    # Check if there are any words
    if words:
        # Return the length of the last word
        return len(words[-1])
    else:
        # If there are no words, return 0
        return 0

s = input('sentence:')
result = length_of_last_word(s)
print(result) 
