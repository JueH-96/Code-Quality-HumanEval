def fix_spaces(text):
    result = ""  # Initialize empty string for output
    i = 0       # Start index at zero
    
    while (i < len(text)):
        if text[i] == " ":   # If the character is a space
            count = 1        
            while ((i+1) < len(text) and text[i+1] == " "): 
                i += 1              # Increment index and counter until we see non-space characters
                count += 1
            
            if count > 2:       # If there are more than two spaces, replace with -
                result += "-"   
            else:               # Else, replace with _
                result += "_" 
        else:                  # Append non-space characters to the output string directly
            result += text[i]  
        
        i += 1                 # Move to next character in input string
    
    return result