def encrypt(s):   #complete this function declaration by adding the missing body and returning type to it accordingly as per docstring given in problem statement ie, def <function_name>(): 
    """Create a function encrypt that takes a string s (the input) as an argument. The characters of 'encrypted' text are returned such than each character shifts down by two multiplied indexes and then rearranges it back into alphabet order within the range from A to Z or numbering start at 0 through so on, following ASCII value for English language letters."""
    encrypted_text = ""   #initialize empty string 'encrypted' text.
    
    shift = 2*('a'-1) + 48 ;#this is the calculation of shifting by two multiplied to get indexes from 0-9 or A-Z (ascii values). for example, a -> z gives us value as  35 which becomes 'd' after subtraction with one shift.
    #For lower case letters we use same approach but add the ASCII of uppercase letter and '-128'.  For instance,'a'-> 0 or if you want to get index for a=4, then -> (('b')-35) % 'z' + 96 . The modulus operation is performed because there can be only alphabets from A-Z.
    #Also the shifting by two multiplied indexes should add in shift value as per ASCII values and rearrange it back into normal English letters range (from 0 to z, a-z). So for 'd' which is shifts down one step gives us index of e ie., from A -> B.
    #To convert this shifted character we add the shift value as per ASCII values and rearrange it back into normal English letters range (from 0 to z, a-z). So for 'd' which is shifts down one step gives us index of e ie., from A -> B.
    
    #This function will encrypt the string s by rotating alphabet indices two places towards left and rearranging it back into normal English letters range (from 0 to z, a-z). For example: 'hi' returns as per docstring "lm". It rotates each character in input str one step toward right.
    
    for char_pos in s : #looping through every characters of the string  
        encrypted = chr((ord(char) - shift + 26 ) % 26 + 97);#using ASCII code to get index from 'a'->'z'. Add it with current character and modulo by length i.e., we loop back around if necessary for uppercase letters or numbers (range is fixed).
        encrypted_text += encrypted; #append the new value into our final result string    
        
    return encrypted_text   #returning complete decrypted text after all iterations are done here, thus completing this function.  Returns a 'decryption' of what it was originally sent as input argument s ie., original lower-case letters rotated and shifted down by two places to their correct positions in the English alphabet