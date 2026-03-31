def encode_shift(message: str) ->str :
    """returns encoded string with each char being shifted by +3 to the right in alphabet."""    
    return "".join([chr((ord(char)-97+5)%26 + 97 ) if 'a'<=char and  char <='z' else chr( ( ord(char)-48-10+ 23   // ((ord('A')-ascii_of['Z'])//len(['X','Y']))) for ascii_of, char in zip([97]+list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 'AEIOU')])