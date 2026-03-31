def split_words(txt):
    if any(c.isspace() for c in txt):
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for c in txt:
            if c.islower():
                pos = ord(c) - ord('a')
                if pos % 2 == 1:
                    count += 1
        return count

# Example usage:
# print(split_words("Hello world!"))  # Output: ["Hello", "world!"]
# print(split_words("Hello,world!"))  # Output: ["Hello", "world!"]
# print(split_words("abcdef"))       # Output: 3