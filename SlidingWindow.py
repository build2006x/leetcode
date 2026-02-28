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
# arr = [1, 2, 3, 7, 5, 10, 5] 
# k = 15
# window = 1
# result = []

# while window <= len(arr):
#       start = 0
#       while start + window <= len(arr):
#              if sum(arr[start:start+window]) == k:
#                     result.append(window)
#              start +=1
#       window +=1

# print(max(result))


### a small explanation of this code like 
## the approach where the we take the window as subarray lenght and move 
### move them each cycle onces the all the window possible lenght is visited means we end up and return the max len in the array

### doing the optimal approach 

### using the two pointer approach 

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# k = 6

# result = []

# left = 0
# right = len(arr)

# while right != 1:
#       print(arr[left:right])
#       if sum(arr[left:right]) == k:
#             result.append(len(arr[left:right]))
#       right -= 1


#### silding window simple sums to get started

# arr = [1, 2, 3, 4, 5]
# k = 3

# start = 0
# end = 3
# result = []

# while end <= len(arr):
#       result.append(sum(arr[start:end]))
#       start +=1
#       end +=1


# print(result)

### what is the problem with above code is about like 
### every cycle we compute every element which leads to the complexity of o(n2)

### if we use the sliding window techinque to make the complexity to o(n)

#### above sums is about finding the all the subarray window size 3 

# arr = [1, 2, 3, 7, 5, 10, 5] 

# k = 15
# left = 0
# right = 3
# windowSum = sum(arr[left:right])

# while right < len(arr):    
#       windowSum += arr[right] - arr[left]
#       left +=1
#       right +=1
#       if windowSum == 15:
#             print(arr[left:right])

      
# print(result)

### this techinque help us to the compute from  the start again and again 

## insead we can moving the left and right pointer we can know the sum of the element 

### this techinque take out of the complexity of o(n) ---reduce from the o(n2)


### so far i encounter the fixed size sliding window sum 

# arr= [9, -3, 3, -1, 6, -5] 

# start = 0
# end = 1

# result = []

# while end<= len(arr):
#       start = 0
#       while start + end <= len(arr):
#             if sum(arr[start:start+end]) == 0:
#                    result.append(arr[start:start+end])         
#             start +=1
#       end +=1

# print(len(result[-1]))

#### this above can we find the both  longest subarray and as well as the smallest one 

# nums = [5,4,-1,7,8]
# left = 0
# right  = 2
# result = []
# windowSum = sum(nums[left:right])

# result.append(windowSum)

# while right < len(nums):
#       windowSum += nums[right] - nums[left]
#       result.append(windowSum)
#       left +=1
#       right +=1

       
# print(result)