def cycpattern_check(s1, s2):
    def cyclics(word):
        return (word[i:] + word[:i] for i in range(len(word)))
    
    return any(c in s1 for c in cyclics(s2))