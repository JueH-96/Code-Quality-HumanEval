def count_nums(arr):
    """Count the numbers which has summed up digits > 0"""
    
    def getDigitSum(numb):  # helper function to calculate digit sums for a number.
        if numb < 0 :   return -1 * (abs(numb) % 9 + 1 )#if negative then absolute of first signed positive digital part will be turned into its negation and rest are counted as per rules described in the question above ie; summed up digits is taken for calculation.
        digitSum = 0   #initialize an empty variable to hold sums, 9's (182 or -36) would add once only because it handles negative numbers properly by multiplying first with abs(numb).
        
        while numb > 0:    #loop through each number until there are no more digits left.  
            digitSum +=numk% 9 +1     #add the digital sum of a single's place to our running total and then divide by '9', so if we got any remainder (like -25), it will become first actual positive integer part, ie; convert into its abs value.
            numb =numk// 9 *10     #divide the number with respecting multiples of ten in order to move next place and handle negative numbers properly when dividing by 'multiple' (like -25/36), because once again, we are dealing only positive part.
        return digitSum   #finally ,return our running total summation variable after all iterations over array elements is completed . 9 should be added as per problem statement to ensure every single number gets covered properly even if there could have been negative numbers in the list or any other unexpected cases which might affect negatives when adding up digits.
    
    numCount = 0   #initialize an empty variable for counting positive integers part of each array element, because we need absolute values to handle负数。  This will hold our final count value at end after all iterations are done over the elements in input list arr as described above ie; summed up digits is taken into account.
    
    #go through every single number (array) part of element, check if it has a positive digital digit or not and then increment that counter accordingly once we find out each such case for counting purpose .  Also keep in mind to handle the edge cases where there could be negative numbers present as per problem statement. So while going over all elements ie; array , at any time when our number part of an element gets a positive digital digit or not, it should get incremented and store that value into numCount variable for counting purpose after checking each case in the list arr . 
    
    #after iterating through every single item (array) check if we found count > 0 then return this to end user. Else simply means there is no such positive digital digit part present inside any element of array so it should just give a response as "No Such Positive Digital Parts Present" else the final result will be returned by running numCount counter and arr list respectively .