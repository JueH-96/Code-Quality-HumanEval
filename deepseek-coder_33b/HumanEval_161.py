def solve(s):
    if not any(char.isalpha() for char in s):
        return s[::-1]
        
    result = ""
    for letter in s:
        if letter.isalpha():
            result += letter.lower() if letter.isupper() else letter.upper()
        else:
            result += letter
    
    return result