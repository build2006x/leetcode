### today i am trying to solve the perivously solved two sum with different 

### i am using the 

# arr =  [2,6,5,8,11]
# target = 14
# left = 0
# right = 2

# while left < len(arr)-1:
#     while right < len(arr):
#          if arr[left]+arr[right] == target:
#                print(left,right)
#          right +=1
#     left +=1
#     right = left + 1

arr = [3, 2, 4]
target = 6

freq = {}

for idx,val in enumerate(arr):
    complement = target - val

    if complement in freq:
         print(freq[complement],idx)
    freq[val] = idx 

### basically how we sovle the problem is 
### about taking complement for each ieration if found means we will return the index with current index 

