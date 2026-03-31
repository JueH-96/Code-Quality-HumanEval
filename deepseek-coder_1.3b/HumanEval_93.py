def encode(message):    
    result = ""  # Initialize the output variable.  
        
    is_upper = 1;      # Boolean flag to determine whether we are at upper case letter or not... initially set as true i.e., first character of each word in message will be changed into an uppercase one by default (as English letters start with a capital). 
    
    for char in message:   # Traverse the input string, 'char' represents individual characters present at any point within this traversal...
        
        if is_upper and ('A'<=char<='Z') :     	# If we are currently on an uppercase character (checked via condition), then convert it to a lower case.  Otherwise keep the same as per requirement, ie., not change anything for non-alphabet characters like punctuation marks etc..
            char = chr(ord('a')+ ord(char) - ord('A'))    # Convert from uppercase letter (ASCII value of a character after 'Z' is subtracted by the ASCII values to convert it into lower case).  The +1 will shift all alphabets one place ahead in english language as per given requirement.
        elif ('a'<=char and char <='z') :         	# If we are currently on a non-uppercase (or previously uppercases) character, then change it into an Upper Case if the previous checked Character is not already so..  Otherwise keep same case for other characters as per requirement.
            pass    # Nothing to do here... just move ahead in loop without changing anything else about this characher because we're only interested on alphabets and non-alphabet character should remain unchanged, according requirements (like spaces or punctuation marks).  If a vowel is found then replace it with the next letter from English Alphabet.
        
        # Add each processed 'characters to our final result string...    
        if ('a'<= char and char <='z') :  			# Vowels will be replaced by following letters in english alphabets (English vowel sequence is: a, e , i , o & u).  If the character processed was lowercase letter then upper case it after replacement.
            if(char== 'a') or char =='e'or char =='i'或 chr('u')) :	# The next alphabetical vowel in English language is b, c etc (so +1 will make sure we get to e and not f for example).  If the character was upper case then after replacement it makes itself lowercase.
                pass   # Do nothing... because there's no need of further action about this characher due requirements mentioned above in loop condition ie., only alphabets are processed, so if a vowel is found we replace that with next English letter and depending upon whether the previous character was upper or lower case it makes itself upercase.
            else :   # If initial checked Character (prev) wasn't already an Upper Case then after replacement make this characeter also LowerCase because of requirements mentioned above in loop condition ie., only alphabets are processed, so if a vowel is found we replace that with next English letter and depending upon whether the previous character was upper or lower case it makes itself upercase.
                # If 'char' already contains an Upper Case then convert this to LowerCase (to match requirements) by adding 32 from ASCII value of char(upper-lowercase).  
        	    		            				# as per requirement, ie., swapping case after replacing vowels with next English alphabet letter.       	    ## Add the processed character into result string...   				            return this 'result' which has been defined in main part of program to get final encoded message..