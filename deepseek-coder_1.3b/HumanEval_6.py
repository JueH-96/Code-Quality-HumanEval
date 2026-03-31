from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    def helper(s, depth):     # Helper function to calculate maximum level of nesting.  
        maxdepth = 0          # initialize the current deepest layer as 1 because we are just starting a new block here for first parentheses '('.      
        
        levels = [0] * len(s)    # Initialize an array with all elements being zero to save level information. This will be our depth tree of blocks in string s, each index represents the corresponding character from start till end (inclusive).  
    
        for i in range(len(s)):  # Traverse through every char '('. We are looking at parentheses block and should not touch them directly. If we find a closing bracket ',', then decrease depth by one because it is coming out from current nested level of nesting (block).  
            if s[i] == "(":     # increase the counter when encounter opening '('. This indicates entering to next parentheses block, so increment maxdepth. 
                levels[maxdepth - i % len(levels)] = depth + 1    # update corresponding index in our level tree with current nesting deepest layer value plus one (as we are currently within this nested structure).  
                ++i             # Increase the loop counter, to skip over any '(' characters.  As soon as it encounters a closing bracket ',', decrease depth by once and move on in our recursion tree starting point below that level block from current parenthese entry (by decrementing i).  
            elif s[i] == ")":    # Decrease the counter when encounter ')'. This indicates leaving out of currently nested section. So, reduce depth by one and move on in our recursion tree starting point below this level block from current parenthese exit (by decrementing i). 
                ++depth & -1   # We are still within same nest as we were just exiting but with previous character being ')', so increase the max-depth by one. This will create correct depth count for all levels of recursion in this block which is used to update our level tree accordingly and later retrieve deepest found information from it via indexing [maxdeep - i%len(levels)]
        return depths          # Return list with maximum nested structure info calculated till now, including the current character.  This will be all levels of depth in one string block represented as integers at corresponding indexes within our final result array (returned by this function).  
    maxdepth = 0              # Initialize counter for level information to track deepest nesting we have seen so far during parsing process, initially set it zero.  This will be used later when returning the output list of all levels in a block represented as integers at corresponding indexes within our final result array (returned by this function).  
    
    depth = 0                # Initialize counter for level information to track current nesting we are currently inside during parsing process, initially set it zero.  This will be used when updating the tree of levels that is represented as integers at corresponding indexes within our final result array (returned by this function).  
    
    depths = []              # Initialize an empty list to hold all maximum depth level info collected from different blocks in string s during parsing process.  This will be used when returning the output, a complete set of max nesting levels for each block represented as integers at corresponding indexes within our final result array (returned by this function).  
    
    nested_blocks = re.findall(r'\((.*?)\)', paren_string )  # Find all groups in the string which represent blocks separated with spaces, and split them using 're' module to get each block separately before we can iterate over it for parsing process because regex find returns list of strings not individual chars.
    
    print(paren_string)           # Print out input so that you know what string is being parsed (just a debugging point).  This will help us understand the structure if any difference observed when running this function on some sample inputs in your test case or other cases as well!  
        
     for block in nested_blocks:    # Iterate over each group, which represents one set of parentheses separated by space. We are looking at different blocks (groups) so increment maxdepth to indicate an entry into new level nesting structure and start it off with depth being 0 as we have just started our recursion tree from this point onward only for these nested groups in the input string s.
         print("In block",block,"found:")        # Debugging points, prints out which group is processing right now (just a debugger).   This will help us understand what's going into different blocks when running our test case or other cases as well!  In this loop we are calling the helper function to process current parentheses block and calculate maximum level of nesting.
         ++maxdepth                   # We have just started with a new nested structure, so increment max-count by one (as each time entry point is different from previous due to depth count starting at 0).   This will be used later when construct our final output list which has all levels information for every block in input string.
     return depths                 # Return the complete result array containing maximum level of nesting info collected till now, including current character processed (all blocks included by this loop and any remaining unprocessed characters if exist). This will be returned at end as our final output list that contains max levels for each block represented in integer form.