def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    def order_word(word):
        """Order characters in a word based on ASCII value, preserving non-ASCII characters' original position"""
        ascii_chars = sorted([c for c in word if ord(c) < 128], key=lambda c: (c.lower(), ord(c)))
        non_ascii_chars = {i: c for i, c in enumerate(word) if ord(c) >= 128}
        
        ordered_word = [''] * len(word)
        ascii_index = 0
        
        for i in range(len(word)):
            if i in non_ascii_chars:
                ordered_word[i] = non_ascii_chars[i]
            else:
                while ascii_index < len(ascii_chars) and any(ord(ascii_chars[ascii_index]) == ord(c) for c in non_ascii_chars.values() if c.islower() == ascii_chars[ascii_index].islower()):
                    ascii_index += 1
                ordered_word[i] = ascii_chars[ascii_index]
                ascii_index += 1
        
        return ''.join(ordered_word)

    return ' '.join(order_word(word) for word in s.split(' '))