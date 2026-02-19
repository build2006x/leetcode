### today i am learning the one of the important pattern in the leetcode 
### as back i am learned the two pointer problem 
### now i am moving to the sliding window concept 

arr1 = [42, 17, 56, 23, 89, 12]
k  = 3

for i in range(len(arr1)-1):
     print(arr1[i:i+k])

### this is how i am thinking to print the element using a fixed 
### window size where the window size will be matined in the printing statment


### working on the sums of sliding window 
"""
Given an array [1, 2, 3, 4, 5] and window size k = 3, find the maximum sum of any subarray of size k.
"""

array  = [1, 2, 3, 4, 5]
start = 0
end  = k - 1
