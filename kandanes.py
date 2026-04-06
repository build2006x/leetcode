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

# nums = [2, 3, 5, -2, 7, -4]
# left = 0
# right = 2
# window = sum(nums[left:right])
# count = 0
# result = 0

# while count != len(nums)-1:
#       if right < len(nums):
#             window += nums[right] - nums[left] 
#             if window > result:
#                   result = window
#       left +=1
#       right +=1
#       count +=1
      
# print(result)

#### so bascially there is problem here to finding the subarray sums with window size we cant use the siliding window pattern
### here we use the kandanes law 

### we preivously used for the majority finding element in the subarray 

nums = [1, 2, 3, 4, 5]
max_val = float('-inf')
current_sum = 0
start = 0
end = 0

for idx,val  in enumerate(nums):
    current_sum = current_sum + val
    if max_val < current_sum:
         max_val = current_sum
         end  = idx
    if current_sum < 0:
        current_sum = 0 
        start = idx 

print(nums[start:end+1])
print(max_val)

### bascially what we are doing is we have to update the start of the measuring length when the starting fresh of index ..
#### we want update the end variable when the maximum sum being update ...

# print(max_val)
### above code is to finding the subarray maximum subarray sum ----  
### like the point of kandanes law 

### extend the sum if postive element are if you find the negative element means start the subbarray sum as fresh as zero  
# ...
# nums = [2, 3, 5, -2, 7, -4]
# start = 0
# window = 0
# max_sum = 0

# sub_left = 0
# sub_right = 0

# while window <= len(nums):
#       start = 0
#       while start + window <= len(nums):
#           code = sum(nums[start:start+window])
#           if code > max_sum:
#                max_sum = code 
#                sub_left,sub_right = start,start+window
#           start +=1
#       code = 0
#       window +=1

# print(nums[sub_left:sub_right])

#### this above code is to print the subarray of the maximum sum in the given array 



