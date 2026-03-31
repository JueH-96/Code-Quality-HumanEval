from typing import List  # for type hinting (optional)
  
def all_prefixes(string: str)->List[str]:    
    return [string[:i] for i in range(1, len(string)+1)][::-1]     
# list comprehension to generate prefix substrings