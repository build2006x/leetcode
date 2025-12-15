#this sum is like appling the operation on a array 

##
nums = [1,2,2,1,1,0]
 
point1 = 0
point2 = 1
endPoint = len(nums) - 1
while point2 != len(nums) - 1:
      if nums[point1] == nums[point2]:
             nums[point1] *=2
             nums[point2] = 0
             nums[point2],nums[endPoint] = nums[endPoint],nums[point2]
      

      
###i work on this like i am knowing the logic 