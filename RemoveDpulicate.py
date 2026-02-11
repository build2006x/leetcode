### today i am working on the removing the duplicate 
### from the sorted array 

# arr = [1,1,1,2,2,3,3,3,3,4,4]
# ##
# actual = []
# get_ritual = set(actual)
# ### adding the element to the set to avoid the duplicate
# for i in arr:
#     get_ritual.add(i)
# get = list(get_ritual)
# ### here we are point to the arr 
# point = 0
# while point < len(get_ritual):
#         arr[point] = get[point] 
#         point +=1
# while point < len(arr):
#       arr[point] = 0
#       point +=1

# print(arr)

#### now thinking in some other approach to solve this problem 

# def remove_duplicates(nums):
#     if not nums:
#         return 0
    
#     j = 0
#     for i in range(1, len(nums)):
#         if nums[i] != nums[j]:
#             j += 1
#             nums[j] = nums[i]
#     return  [nums[i] for i in range(0,j+1)] # length of unique array


# result = remove_duplicates([1,1,1])
# print(result)

#### this is another brute force 

### now i am trying to convert the above brute force approach using the two pointer approach 

### in place method i am going to try now 

def RemoveDuplicate(nums):
     track = 0
     point = 1
     while point < len(nums):
          if nums[track] != nums[point]:
                track +=1
                nums[track] = nums[point]
          point +=1
     return nums[0:track+1]

result = RemoveDuplicate([1,1,1,2,3,3,3,4,4])
print(result)