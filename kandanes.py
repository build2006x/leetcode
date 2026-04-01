# nums = [2, 3, 5, -2, 7, -4]

# window = 1
# clear = 0
# result = 0

# while window < len(nums):
#       start = 0 
#       while start + window <= len(nums):
#             clear += sum(nums[start:window+start])
#             print(nums[start:window+start])
#             if clear > result:
#                   result = clear
#             start +=1
#             clear = 0
#       window  +=1

# print(result)

            

#### above code is all about the about the finding the subarray using the brute force method to find apart 

nums = [2, 3, 5, -2, 7, -4]
left = 0
right = 2
window = sum(nums[left:right])
count = 0
result = 0

while count != len(nums)-1:
      if right < len(nums):
            window += nums[right] - nums[left] 
            if window > result:
                  result = window
      left +=1
      right +=1
      count +=1
      
print(result)

