### today i am learning the one of the important pattern in the leetcode 
### as back i am learned the two pointer problem 
### now i am moving to the sliding window concept 

# arr1 = [42, 17, 56, 23, 89, 12]
# k  = 3

# for i in range(len(arr1)-1):
#      print(arr1[i:i+k])

### this is how i am thinking to print the element using a fixed 
### window size where the window size will be matined in the printing statment


### working on the sums of sliding window 
"""
Given an array [1, 2, 3, 4, 5] and window size k = 3, find the maximum sum of any subarray of size k.
"""

# nums = [5, 5, 5] 
# k = 15
# window = 1
# start = 0
# result = []
# range = 1

# while window < len(nums):
#       while window < len(nums):
#             if sum(nums[start:window]) == k:
#                    print(nums[start:window])
#                    result.append(len(nums[start:window]))
#             window +=1
#             start  +=1  
#       range +=1
#       start = 0
#       window = range 

# if not result:
#       print('no subarray exists')
#       print(result)
# else:
#       print(max(result))



##### i am incountering the finding the largest subarray ...
arr = [1, 2, 3, 7, 5, 10, 5] 
k = 15
window = 1
result = []

while window <= len(arr):
      start = 0
      while start + window <= len(arr):
             if sum(arr[start:start+window]) == k:
                    result.append(window)
             start +=1
      window +=1

print(max(result))


### a small explanation of this code like 
## the approach where the we take the window as subarray lenght and move 
### move them each cycle onces the all the window possible lenght is visited means we end up and return the max len in the array