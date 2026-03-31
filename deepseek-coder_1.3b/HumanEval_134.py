def check_if_last_char_is_a_letter(txt):  
    words = txt.split() # splitting the string into list of words based on spaces    
        
    return all((word[-1].isalpha()) for word in words) and not any (len(word[0]) > 2 or len(''.join([char if char.isalpha() else '' for char in word]))== 1 ) # checking each condition: the last character is alphabetical, no part of a bigger sequence starts with it
```
Test this function to see how well your understanding has progressed up till now :-D Hope you find above code helpful. Remember that words are separated by spaces in given sentence so make sure they're split correctly when passing string into the function accordingly and consider all edge cases for input strings, such as empty space or only alphabets at end of a word etc.,