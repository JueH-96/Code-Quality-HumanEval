import re
def file_name_check(file_name):
    pattern = r'^[a-zA-Z]\w{0,2}\.\w+\.(exe|dll|txt)$'  # This regex checks for filename format from your examples. Modify as needed to suit different requirements of file names.  
    
    if re.match(pattern,file_name):        
        return 'Yes'                        # Return Yes on match and No otherwise when pattern does not match the string or is None (not valid).  Here we do a quick check for matching in regex but you can also use more robust methods to validate file names depending upon requirements.  
    else:                                  
       return "No"