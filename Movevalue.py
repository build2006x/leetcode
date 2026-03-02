### i am working on the sum which have to remove the the front  the remaining values
nums = [0,1,2,2,3,0,4,2] 
val = 2

point1 = 0 
point2 = len(nums) - 1
count = 0 

while point1 < point2:
     if nums[point1] == val and nums[point2] != val:
            nums[point1],nums[point2] = nums[point2],nums[point1]
            point1 +=1
            point2 -=1
     elif nums[point1] == val and nums[point2] == val:
            point2 -=1




        
