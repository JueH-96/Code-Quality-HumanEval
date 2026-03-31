def count_distinct_characters(string):    
    string = set((c.lower() for c in string if str(c).isalpha())) # filter out non-alphabetic characters and convert to lowercase 
                                                                   # before adding into a Set (which inherently removes duplicates)
                                          
    return len(string)