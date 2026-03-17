### today i am working on the sum of sorting the zero 

# nums = [2,0,2,1,1,0]

### we have to sort this arr with duplicate 

### ---- we choosing the bubble sorting algorithm first to short this problem 

# Pointer1 = 0
# Pointer2 = 1
# lenght = len(nums)

# while lenght != 0:
#         while Pointer2 < lenght: 
#             if nums[Pointer1] > nums[Pointer2]:
#                 nums[Pointer1],nums[Pointer2] = nums[Pointer2],nums[Pointer1]
#             Pointer1 +=1
#             Pointer2 +=1
#         Pointer1 =0
#         Pointer2 = Pointer1 + 1
#         lenght -=1

# print(nums)


#### this is what the bubble sort look like 

# from collections import Counter

# nums = [2,0,2,1,1,0]

# nums = Counter(nums)

# print(nums)


### like the brute how we can do means of take the count of the each number and fill based according to that 


### optimal way of sorting the this array using two pointer method of doing this 

nums = [2,0,2,1,1,0]

low = 0

high = len(nums) - 1 


while low < high:
      if nums[low] > nums[high]:
             nums[low],nums[high] = nums[high],nums[low]
             high -=1
      elif nums[low] < nums[high]:
             low +=1
     
print(nums)


### i am working with the above code to think in two pointer to solve this problem 
