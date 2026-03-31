from typing import List
  
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:    
    """Filter an list of strings only for ones that start with a given 'prefix'.
     >>> filter_by_prefix([], "a")  # Returns [] as there are no elements in the string array.
     >>> filter_by_prefix(['abc', 'bcd','cde','array'],'a')   # ['abc'] is returned because it starts with prefix a and others do not start by this character hence filtered out before returning result     """ 
    return [s for s in strings if s.startswith(prefix)]