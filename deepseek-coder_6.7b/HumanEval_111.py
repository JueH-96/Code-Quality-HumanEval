def histogram(test):
    test = test.split() # split input string into list of words
    freq_dict = {}      # initialize empty dictionary to store frequency count of each word
    
    for letter in test:  # iterate over each word (letter) in the list
        if letter not in freq_dict:  
            freq_dict[letter] = 1      # If word is not yet in dictionary, add it with a value of 1.
        else:    
            freq_dict[letter] += 1    # Otherwise increment its count by one.
            
    max_freq = max(freq_dict.values()) if freq_dict else 0   # Find the maximum frequency
    
    return {key: value for key, value in freq_dict.items() if value == max_freq} # Return dictionary with letters having highest frequency only.