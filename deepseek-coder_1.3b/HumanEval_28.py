from typing import List

def concatenate(strings: List[str]) -> str:  # assuming strings is a non-empty array of string values. Change to accommodate empty list scenario if necessary; otherwise, just return '' in the case where input would be an空列表 ([]) or None instead which can cause runtime error
    """ Concatenate List[str] into Single String using join() method 
    >>> concatenate(["I", "love","Python"]) # 'I love Python'  => Returned string from the function. Change as per your requirement if you want to have different separator or add more elements in list, also change type of input accordingly (str) into a List[int], etc
    """ 
     return ' '.join(strings)      # join all strings using space (' '), can be changed according the case. This method returns single string containing given iterable’s items formatted by str and joined with specified separator, in this instance `str` is a list of elements (string). If any element not serializable it will raise TypeError