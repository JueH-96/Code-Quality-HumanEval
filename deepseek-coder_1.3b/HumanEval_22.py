from typing import List, Any
  
def filter_integers(values:List[Any])->List[int]:    
    return [i for i in values if isinstance(i, int)] #list comprehension to get integers from the list