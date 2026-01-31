### -- today i working on the insertion sorting algorithm 
### -- the point is all if not left element is not there we dont wanted to check 
### -- is the left element is being there means we have to sort them

nums = [5, 4, 3, 2, 1] 

for i in range(0,len(nums)-1):
    for j in range(0,len(nums)-1):
         if nums[j+1] < nums[j]:
               nums[j+1],nums[j] = nums[j],nums[j+1]

print(nums)  





