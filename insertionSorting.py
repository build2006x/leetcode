### -- today i working on the insertion sorting algorithm 
### -- the point is all if not left element is not there we dont wanted to check 
### -- is the left element is being there means we have to sort them

nums = [5, 4,2,1] 

for i in range(0,len(nums)-1):
    for j in range(0,len(nums)-1):
         if nums[j+1] < nums[j]:
               nums[j+1],nums[j] = nums[j],nums[j+1]

print(nums)  


### i am getting understaing much more of the outer loop in the above code where we leave a edge case of 0 to len(nums1)-1
### like they are 4 elements means each pass of outer loop we know one element will defintely will placed corretly in the right position 
### so its better to go for how many elements are being in the give array 

### let me do this insertion sorting in the recursion approach....

###---




      
      
     



