def minSubArraySum(nums):

The function is passed as 'nums', which could be an empty list. But in the examples, the given arrays are non-empty.

So perhaps we should consider that nums can be empty. Wait no: wait the problem says "non-empty sub-array", but the function requires at least one element to form a subarray. So if nums is empty, what's the minimal sum? It's undefined or the function might throw an error.

But perhaps in code, we can assume that nums has at least one element. Or else handle it by raising an error or returning None.

Wait but looking at the examples: both examples have non-empty arrays. So maybe the function is intended to be called with a non-empty array.

So in our code, perhaps we can proceed under the assumption that the input is not empty. But what if someone passes an empty list? Then our code may crash.

But since it's part of the problem description, perhaps in this case, for the given examples and function signature, I should write the code assuming that nums is non-empty.

So the steps are:

1. Initialize current_min and global_min with the first element.

Wait no: because if all elements are negative, the minimal sum could be the sum of the entire array. Wait wait no: for example, in [-5,-3], the minimal subarrays would be either -5 or -8 (sum of both). So which is smaller? -8 < -5. So the minimal sum is -8.

Wait but that's not possible because if you take all elements as a subarray, their sum is -8, which is less than any individual element.

So in this case, when all numbers are negative, the minimal sum would be the sum of all elements (since adding more negatives makes it even smaller).

But wait no: No, wait for example [-1,-2,-3]. The sum is-6. But if you take just -3, that's a sum of-3 which is larger than -6.

Wait no: Wait in terms of numerical value, -6 < -3. So the minimal sum would be achieved by taking all elements (sum=-6), since it's smaller than any individual element.

So yes, when all elements are negative, the minimal sum is the sum of all of them.

But wait in the case of [-1,-2], minimal is sum -3, but if you have a subarray like [-2], which is larger (less negative) than the total sum. Wait no: wait in terms of numerical value, -3 is less than -2, so it's smaller.

Wait this brings up an important point: when comparing sums, we are looking for the minimal possible sum, which could be more negative or less positive.

So yes, if all elements are negative, adding all of them gives a smaller (more negative) sum, hence minimal.

But wait in our algorithm above, does it capture that?

Wait let's test with [-5,-3].

current_min starts as -5. global_min=-5.

i=1: current element is-3.

current_min = min(-3, current_min_prev (-5)+ (-3)=-8). So between -3 and -8: which is smaller? -8 is less than -3 (since it's more negative), so current_min becomes -8. Then global_min updates to min(-5,-8)=-8.

So yes, the algorithm captures that.

Another test case: [ -1, 2, -3 ].

What would be the minimal sum?

Possible subarrays:

[-1] →-1

[-1,2]→1

[-1,2,-3]→-2

[2]→2

[2,-3]→-1

[-3]→-3.

So the minimal is -3 (from [-3]) or wait no: Wait sum of [-1,2,-3] is (-1)+2+(-3)= -2. So among all subarrays:

The sums are:

-1, 1, -2, 2, -1, -3.

So the minimal is -3 (from [-3]) and also from [ -1,2,-3 ] sum is -2? Wait no: wait I think I made a mistake in my earlier calculation. Let me compute:

Wait [-1,2] sum = (-1)+2=1

[-1,2,-3]= (-1)+2+(-3)= (-4 + 2)=-2.

[2,-3]= (2)+(-3)= -1.

So the subarrays and their sums are:

-1 → -1

-1,2 →1

-1,2,-3→ -2

2→2

2,-3→-1

-3→-3.

So the minimal sum is -3 (from [-3]) and also from [ -1,2,-3 ] it's -2. So the minimal is -3.

But in this case, the algorithm would process as follows:

current_min starts with -1 (i=0). global_min=-1.

i=1: element 2.

current_min = min(2, current_min_prev (-1) +2=1). So between 2 and 1, the smaller is 1. So current_min becomes1. Then global_min remains -1.

Then i=2: element-3.

current_min = min(-3, current_min_prev (1)+ (-3)= -2).

So between -3 and -2: which is smaller? -3 < -2. So current_min=-3. Then global_min updates from -1 to -3.

Which is correct because the minimal sum is-3.

But wait in this array, there's a subarray [ -3 ] with sum -3, and another subarray that includes all three elements which sums to -2. So the minimal is indeed -3.

So our algorithm captures that correctly.

Another test case: [ 5, -1, 4 ].

Possible minimal sum would be min of:

[5] →5

[5,-1]→4

[5,-1,4]→8

[-1] →-1

[-1,4]→3

[4]→4.

So the minimal is -1. The algorithm should capture that.

Processing:

current_min starts as5 (i=0). global_min=5.

i=1: element-1.

current_min = min(-1, 5 + (-1)=4) →-1 is chosen. Global_min becomes min(5,-1)=-1.

i=2: element4.

current_min = min(4, current_min_prev (-1)+4=3). So between4 and3→3 is smaller. But wait no: min(4,3) is 3. Wait, but the algorithm says:

Wait for i=2 (element4):

current_min is min(4, current_min_prev +4).

current_min_prev was -1.

So current_min = min(4, (-1)+4=3). So which is smaller? 3 <4 → so current_min becomes3. Then global_min remains-1.

But the minimal sum in this array is-1 (from [-1]), and the algorithm correctly keeps that as the global_min.

So yes, it works.

Thus, the approach of tracking current_min and updating it based on whether adding the current element to current_min or starting a new subarray with just the current element gives a smaller sum seems solid.

Now, let's think about how to implement this in code.

The steps would be:

1. Check if the array is empty. If so, perhaps return None or raise an error. But given the problem statement examples, perhaps we can assume it's non-empty. So for now, proceed without handling that case, but perhaps in code, add a check to avoid index errors.

Wait wait no: in Python, trying to access nums[0] when len(nums) is zero would throw an IndexError. So in code, perhaps first handle the empty list by returning None or raising ValueError.

So:

if not nums:
    return None  # Or raise ValueError("Empty array")

But since the problem statement's examples have non-empty arrays, perhaps it's acceptable to assume that the function is called with a non-empty list. But for robustness, better to handle the empty case.

Wait but the minimal subarray sum in an empty array is undefined. So perhaps if nums is empty, we can return None or raise an error.

But since it's not specified in the problem statement, perhaps proceed as follows:

if len(nums) == 0:
    return None

Else proceed.

So in code:

def minSubArraySum(nums):
    if not nums:
        return None  # Or maybe raise ValueError
    current_min = global_min = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        if current_min < global_min:
            global_min = current_min
    return global_min

Wait wait no: that's not correct. Wait in the code above, we're initializing current_min and global_min as nums[0], then for each subsequent number (starting from index 1), set current_min to min(num, current_min + num). Then update global_min if current_min is smaller.

But this would work for all cases except when all elements are negative. Wait no, earlier test cases showed that it works.

Wait wait no:

Wait the code initializes current_min and global_min as nums[0]. Then for each subsequent number in nums (starting from index 1), current_min is set to min(num, current_min + num). Then if this new current_min is less than global_min, then update global_min.

But wait, what about when adding the next element gives a smaller sum? Because sometimes you need to consider that starting a new subarray at the current position may yield a better (smaller) sum than continuing from the previous one.

Wait in the code above, for each num:

current_min = min(num, current_min + num)

That's correct. So if adding the current number to current_min is better (i.e., gives a smaller sum), then we continue; otherwise, start fresh with this number as the new subarray.

Yes, that logic seems right.

But what about when all numbers are negative? As in [-5,-3], which should give a minimal sum of -8. Let's see:

current_min starts at-5 (global_min=-5).

next num is-3:

current_min = min(-3, (-5)+ (-3)=-8). So current_min becomes-8. Then global_min updates to-8.

Which is correct.

Another test case: [ -2, 1, -3 ].

Processing:

current_min and global_min start at-2.

Next num=1:

current_min = min(1, (-2)+1=-1). So current_min is-1. Global_min remains-2 (since -1 > -2? Wait no: wait in terms of numerical value, which is smaller? -2 < -1 → so global_min should remain at-2.

Wait no:

global_min is initialized to-2.

current_min after processing 1 is min(1, (-2)+1=-1)→-1. Then since current_min (-1) is greater than global_min (-2), global_min remains -2.

Next num: -3.

current_min = min(-3, (-1)+(-3)=-4). So between -3 and -4 →-4 is chosen as current_min. Now compare to global_min (-2): since -4 < -2 (because in Python, negative numbers work such that -4 is less than -2), so global_min updates to-4.

So yes, the minimal sum is correctly captured as-4, which comes from adding 1 and then -3: wait no. Wait in this case:

Wait [ -2 ] →sum=-2

[ -2,1 ]→sum=-1

[ -2,1,-3 ]→sum=(-2)+1+(-3)=-4.

So yes, that's the minimal sum of-4, which is captured by global_min as it becomes-4 after processing the third element.

Thus, the code works for this case.

Another test: [5, -1, 4].

Initial current_min and global_min=5.

Next num=-1:

current_min = min(-1, 5 + (-1)=4) →min(-1,4) is-1. So current_min becomes-1. Then since -1 <5 (the initial global_min), global_min updates to-1.

Next num=4:

current_min = min(4, (-1)+4=3). So between 4 and3→3 is smaller. So current_min=3. Now compare to global_min (-1): since3 >-1, no change in global_min.

Thus, the minimal sum remains at-1, which is correct as [ -1 ] gives that sum.

So the code works for this case.

Another test: [2,-1,2,-4].

What's the minimal subarray?

Possible candidates:

[2] →2

[2,-1]→1

[2,-1,2]→3

[2,-1,2,-4]→-1

[-1]→-1

[-1,2]→1

[-1,2,-4]→(-1)+2+(-4)=-3.

[2,-4]→( -2 )

Wait wait:

Wait 2 + (-1)=1; then +2=3; then +(-4)= -1.

Subarray [ -1 ] sum is-1.

Subarray [ -1,2 ]: sum is1.

Subarray [ -1,2,-4 ]: sum is ( -1 )+2=1→1+ (-4)= -3.

Subarray [ 2,-4 ]: sum is -2.

So the minimal sum here would be-4? Wait no:

Wait wait, perhaps I missed a subarray. Let's see:

Wait the array is [2,-1,2,-4].

Possible subarrays:

Indices (0-based):

[0] →2

[0,1]→1

[0,1,2]→3

[0,1,2,3]→-1.

[1]→-1

[1,2]→( -1 )+2=1

[1,2,3]→ (-1)+2+(-4)= -3.

[2]→2

[2,3]→ (2) + (-4)= -2.

[3] →-4.

So the minimal sum is-4 (from [3]), which is smaller than all other sums.

But let's see what the code does:

current_min starts as2. global_min=2.

Next num=-1:

current_min = min(-1, 2+ (-1)=1)→min(-1,1) is-1. So current_min becomes-1. Now, since -1 <2 →global_min updates to-1.

Next num=2:

current_min = min(2, (-1)+2=1). min(2,1)=1. So current_min=1.

Now compare to global_min (-1): 1 >-1 →no change in global_min.

Next num=-4:

current_min = min(-4, (1) + (-4)= -3). Between-4 and-3→-4 is smaller. So current_min becomes-4. Now, since-4 < global_min (-1), update global_min to-4.

Thus, the code correctly captures that the minimal sum is-4.

So yes, this approach works.

Now, what about when all elements are positive? For example: [3,1,2].

The minimal subarray would be any single element, which is 1 (the smallest). Wait no:

Wait wait in terms of minimal sum, if all numbers are positive, the minimal sum would be the smallest number. Because adding more positive numbers only increases the sum.

But let's see:

In [3,1,2], the possible subarrays:

[3]→3

[3,1]→4

[3,1,2]→6

[1] →1

[1,2]→3

[2]→2.

So minimal sum is1 (from [1]).

The code would process as follows:

current_min and global_min start at3.

Next num=1:

current_min = min(1, 3+1=4) →1. So current_min becomes1. Since1 <3, global_min updates to1.

Next num=2:

current_min = min(2, 1 +2=3). min is2. Now compare to global_min (1): since2>1, no change in global_min.

Thus, the minimal sum is correctly captured as1.

But wait, the code returns global_min which would be1, but wait in this case [1] is part of the array and gives a sum of1, which is indeed the minimal possible. So correct.

Another test: [ -2, 3, -1 ].

The possible subarrays:

[ -2 ] →-2

[ -2,3 ]→1

[ -2,3,-1 ]→0.

[3] →3.

[3,-1 ]→2.

[-1] →-1.

So the minimal sum is-2 (from [ -2 ]) and also from [ -1 ] which is-1. So the minimal is-2.

Wait no:

Wait in this array, what's the minimal sum?

Looking for the smallest possible sum:

[ -2 ] sum=-2

[-2,3] sum=1

[-2,3,-1] sum=0

[3] sum=3

[3,-1] sum=2

[-1] sum=-1.

So the minimal is-2 (from [ -2 ]) and also from [ -1 ] which is-1. So the smallest is-2.

Wait no: wait in terms of numerical value, -2 < -1 → so yes, the minimal sum is-2.

Let's see what the code does:

current_min starts at-2 (global_min=-2).

Next num=3:

current_min = min(3, (-2)+3=1). So current_min becomes1. Since1 >-2, no change in global_min.

Next num=-1:

current_min = min(-1, 1 + (-1)=0) →min is-1. Now compare to global_min (-2): since -1 >-2 (because -2 is less than -1), the global_min remains at-2.

Thus, the code returns-2 as the minimal sum, which is correct because the subarray [ -2 ] gives that sum.

But wait in this case, the minimal is achieved by just taking the first element. The algorithm correctly captures that.

Another test: [ 1, 2, 3, -4, 5 ].

Possible minimal sum:

Looking for the most negative possible.

Subarrays:

[ ... , -4, ... ] but adding elements before and after may give a more negative sum.

Wait let's compute some subarrays:

Sum of [1,2,3,-4]→(6) + (-4)=2.

Sum of [3,-4] →-1.

Sum of [-4] →-4.

Sum of [ -4,5 ] →1.

So the minimal sum is-4 (from [ -4 ]) or wait:

Wait also, if we take [ 1,2,3,-4,5 ]: sum is7 + (-4) =3; not minimal.

But what about a subarray that includes elements before and after -4? For example, [3,-4,5]→(3)+(-4)= -1 +5=4. So the minimal in this array would be-4 (from [ -4 ]).

The code should capture that:

current_min starts at1.

global_min=1.

next num=2:

current_min = min(2, 1+2=3) →min is2. Since2>1, no change in global_min.

next num=3:

current_min = min(3, 2+3=5)→3>1 →no change.

global_min remains1.

next num=-4:

current_min = min(-4, (3)+ (-4)= -1). So between-4 and-1: min is-4. Now compare to global_min (1): since-4 <1, update global_min to-4.

next num=5:

current_min = min(5, (-4) +5=1). Between5 and1→1 is smaller. So current_min becomes1. Since1 >-4, no change in global_min.

Thus, the minimal sum is correctly captured as-4.

So all test cases seem to be handled correctly by this algorithm.

Now, what about when there are multiple elements with varying signs? For example: [ -1, 2, -3, 4 ].

The minimal sum could be from subarrays like [ -1,2,-3 ] which sums to-2, or maybe [ -3 ] which is-3. Let's compute:

Subarrays:

[ -1 ] →-1

[ -1,2 ]→1

[ -1,2,-3 ]→ (-1)+2=1 + (-3)= -2.

[ -1,2,-3,4 ]→ ( -2 ) +4=2.

[ 2 ]→2

[ 2,-3 ]→-1

[ 2,-3,4 ] →( -1 )+4=3.

[ -3 ] →-3

[ -3,4 ]→1.

[4 ]→4.

So the minimal sum is-3 (from [ -3 ]) or maybe another subarray?

Wait no: wait in this array, the minimal sum is indeed-3. But let's see what the code does:

current_min starts at-1 →global_min=-1.

next num=2:

current_min = min(2, (-1)+2=1)→min is1 (since 2>1). Wait no: wait current_min will be the minimum between the new number and the previous current_min plus this number. So for 2, it's min(2 vs -1 +2=1). The min of those two is1. But wait wait:

Wait no: when processing the second element (which is2), the code computes current_min as the minimum between taking just that element (2) or adding it to the previous subarray sum (current_min was-1, so -1+2=1). So current_min becomes the min of 2 and1, which is1. Since1 > global_min (-1), no change in global_min.

Next num=-3:

current_min = min(-3, (1) + (-3)= -2). So between-3 and-2: min is-3. Now compare to global_min (-1): since-3 < -1 →update global_min to-3.

Next num=4:

current_min = min(4, (-3)+4=1). Between4 and1→min is1. Since1 >-3 (global_min), no change.

Thus, the code captures the minimal sum as-3, which comes from taking just the third element [ -3 ] or perhaps a subarray that includes it? Wait in this case:

Wait wait when we take current_min as-3 after processing the third element (-3):

But how did we get there?

The previous current_min was1 (from the second element). Then for the third element, which is-3, current_min is min(-3, 1 + (-3)= -2).

So between-3 and-2: min is-3. So this represents taking a new subarray starting at this element (i.e., [ -3 ]) or continuing the previous subarray.

Thus, the minimal sum is correctly captured as-3.

But wait in reality, there's a longer subarray that includes elements before and after which might have an even lower sum? Wait no:

Wait let's see: what about [2,-3] →sum is-1. That's higher than-3.

What about [-1,2,-3]→ sum is (-1)+2=1 + (-3)= -2, which is higher than-3.

So yes, the minimal is indeed-3, from taking just [ -3 ].

Thus, the code works.

Another test: [ 4, -1, 2, -5, 3 ].

Possible minimal sum:

Looking for the most negative subarray.

Subarrays including -5 might be candidates. Let's see:

[ ... , -5, ... ]

For example:

[4,-1,2,-5] →sum is (4-1)=3 +2=5 -5=0.

[ -1,2,-5 ]→(-1)+2=1 -5=-4.

[ 2,-5 ]→-3.

[-5 ]→-5.

So the minimal sum would be-5 (from [ -5 ]) or perhaps a subarray that includes more elements before it?

Wait:

What about [4,-1,2,-5,3]: sum is (4-1)=3 +2=5 -5=0 +3=3.

Not helpful.

[ -1,2,-5,3 ] → (-1)+2=1 -5=-4 +3=-1.

So no, the minimal is still-5.

But let's see what the code does:

current_min starts at4 (global_min=4).

next num=-1:

current_min = min(-1, 4 + (-1)=3) →min is-1. Since-1 <4, update global_min to-1.

next num=2:

current_min = min(2, -1+2=1). min is1 (since2>1? Wait no: wait min(2 vs1) is1. So current_min becomes1. Now since1 >-1 (global_min), no change in global_min.

Wait no: wait the code uses:

current_min = min(num, current_min + num)

So for this step:

num=2

current_min was -1 from previous step.

Compute temp = current_min + num →-1+2=1.

Then new_current_min = min(2, 1) →1.

Since1 is less than the previous current_min (-1)? Wait no: wait in terms of numerical value, but for minimal sum, we're looking for the smallest possible number (most negative). So when adding a positive number to a negative current_min could result in a higher or lower sum depending on the numbers.

Wait wait this step might be causing confusion. Let me re-express it:

At each step, current_min is updated as the minimum between taking the new element alone or adding it to the previous subarray's sum (current_min). So for num=2:

previous current_min was-1.

new_current_min = min(2, -1 + 2) →min(2,1)=1.

So now current_min is1. But since we're looking for the minimal sum, which could be more negative, why are we updating to a higher (less negative) number?

Ah! Wait no: wait in this case, when you add 2 to -1, you get1, which is better than taking just 2 alone (which is2). So current_min becomes1.

But since our global_min was-1, and now we have a new current_min of1, which is higher (less minimal), the global_min remains at-1.

Wait but perhaps I'm misunderstanding: no, wait when you process num=2:

The possible subarrays ending at this position are either [2] or [-1,2]. The sum for [ -1, 2 ] is1, and for [2] it's2. Since we're looking for the minimal sum (most negative), which would be the smaller of these two sums. But wait in terms of numerical value, 1 is larger than-1.

Wait no: wait in this case, when considering whether to extend the previous subarray or start a new one, we take whichever gives the smallest possible sum (more negative). So for num=2:

Option1: take just 2 →sum=2.

Option2: add to previous current_min (-1) →sum=-1+2=1.

So between these two options, which is smaller? In terms of numerical value, 1 is larger than-1. Wait no: wait in this context, "smaller" refers to the sum being less (more negative). So 2 vs1: 1 is larger than2? No, numerically, 1 <2.

Wait I'm getting confused here. Let me think again:

When we have current_min = min(num, current_min + num), it's about finding the minimal possible sum for subarrays ending at this position. So if adding the new number to the previous current_min gives a smaller (more negative) sum than taking the new number alone, then we take that.

Wait no: wait when you have current_min as-1 and add2, you get1. But 1 is larger than-1. Wait no:

Wait in terms of numbers, -1 <1 <2.

But we're looking for minimal sum (most negative). So between taking the new number alone (sum=2) or adding it to previous subarray (sum=1), which one is smaller? Well, 1 is larger than-1, but wait no:

Wait current_min before this step was-1. Then when we process the next element (2):

The possible options are:

- Start a new subarray with just 2 → sum=2.

- Extend the previous subarray by adding 2 to its sum (-1 +2=1).

So between these two, which is smaller? In terms of numerical value, 1 <2. So the minimal (more negative) would be1? Wait no: wait in terms of numerical value, -5 is smaller than-3, but when we're just considering sums, a lower sum is more minimal.

Wait no: I think I'm getting confused here. The way the code works is that current_min represents the minimal sum achievable by any subarray ending at the current position. So for each new number, you can either start a new subarray (sum=num) or continue the previous subarray (sum=current_min + num). You take whichever is smaller.

Wait no: wait in this case:

current_min before processing 2 was-1 (from the previous step).

Processing 2:

Option1: sum = current_min + 2 → -1 + 2=1.

Option2: sum =2.

So between these, which one is better? We take the minimum of these two options. min(1,2)=1.

But wait we're looking for the minimal possible sum (most negative). So if both options are positive or less negative than before, then perhaps this isn't helping us find a more minimal sum.

Wait no: in this case, since 1 is larger than-1, but the global_min was already set to-1. So even though current_min becomes1 here, the global_min remains at-1 because that's the smallest we've seen so far.

But wait I think I'm missing something: perhaps when you process the third element (2), the minimal sum ending at this position is1, but since our global_min was already-1 from the second element (-1), which is smaller than1, the global_min doesn't change. So in this case, the code correctly keeps the global_min at-1.

But wait let's proceed further:

Next num=-5 (fourth element):

current_min is1 (from previous step).

Compute new_current_min = min(-5, 1 + (-5)= -4). The minimum between-5 and-4 is-5. So current_min becomes-5.

Since-5 < global_min (-1), we update global_min to-5.

Next num=3:

current_min is-5 (from previous step).

Compute new_current_min = min(3, -5 + 3= -2). The minimum between3 and-2 is-2. So current_min becomes-2.

Since-2 > global_min (-5), no change to global_min.

Thus, the minimal sum found is-5, which corresponds to the subarray [ -5 ] or perhaps a longer one that includes elements before it? Wait let's see:

Wait when we processed num=-5 (fourth element), current_min became-5. That could represent either taking just [-5] or continuing from the previous subarray.

But what was the previous subarray?

Before processing -5, current_min was1 (from processing 2). So adding-5 to that gives1 + (-5)=-4, but we took the min between-5 and-4, which is-5. That means we decided to start a new subarray at this point, i.e., just [-5], because its sum (-5) is smaller than continuing from the previous subarray (sum=-4).

So yes, the minimal sum is indeed-5, achieved by taking just the fourth element.

Thus, the code correctly captures that.
</think>

The minimal sum of any contiguous subarray in the given array is \boxed{-5}.