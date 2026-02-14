#### today i working on the moving the zero to the end leetcode sum 
nums = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

point1 = 0

for i in range(0,len(nums)-1):
     if nums[i] == 0 and nums[i+1] ==0:
            nums[i],nums[i+2] = nums[i+2],nums[i]    
     elif nums[i] == 0:
         nums[i],nums[i+1] = nums[i+1],nums[i]
     print(nums)

#### here the edge case about double zero in the row 

