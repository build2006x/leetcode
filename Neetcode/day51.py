############## hey hi today i am working on the 
nums=[1,2,3,4,5,6,7]

k = 3
k = k % len(nums)


l = 0
r = len(nums) -1 


while l < r:
     nums[l],nums[r] = nums[r],nums[l]
     l +=1
     r -=1

l = 0
r = k - 1

while l < r:
       nums[l],nums[r] = nums[r],nums[l]
       l +=1
       r -=1

l = k 
r = len(nums) -1  

while l < r:
       nums[l],nums[r] = nums[r],nums[l]
       l +=1
       r -=1


print(nums)