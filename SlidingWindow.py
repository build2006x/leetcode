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


nums = [10, 5, 2, 7, 1, 9]
k = 15
window = 1
start = 0
result = []

while start != len(nums)-2:
      while window !=len(nums):
            if nums[start:window] == k:
                   result.append(len(nums[start:window]))
            window +=1
            start  +=1
      start = 0
      window +=1   
                    
print(result)