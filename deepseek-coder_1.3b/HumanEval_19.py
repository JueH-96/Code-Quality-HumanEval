from typing import List
  
def sort_numbers(numbers : str) -> str {
    num2word = ['zero', 'one' , ‘two’,'three','four','five','six','seven','eight','nine'] #mapping ordinal to word. In Python, strings are sequences of characters and therefore can be used for this purpose too as well because we convert them into a list
    num2num = {v: i for i, v in enumerate(num2word)} 	# creating dictionary that will map words back onto their corresponding ordinal numbers or 'keys' from the previous step. In Python dictionaries can be used to quickly retrieve and assign values as well because they are hash tables too
    nums_ascii = sorted([ord(c) for c in re.split('\W+',numbers)] + [10]) 	# converting our string into a list of ASCII numbers, separating words by non-word characters and sorting the result using Python's builtin function
    num_words=[num2word[i] for i in sorted(nums_ascii ,key = lambda x: (x % 10) * 4 + ((x // 10)))] # mapping back to word. The '//' operator is used instead of '/', it will give the floor value, which means we convert an integer into a decimal number and then truncate off any decimals
    return " ".join(num_words)  	# Join all elements in nums with space as delimeter  to get string. The join() method joins two or more strings together using some specified separator (string here). By default, it uses a single spacé character but can be defined by any other string
}