### today i am sovling the leetcode problem - 1877 
# 1877. Minimize Maximum Pair Sum in Array
## the problem is finding the minimized maxium pair sum 

nums = [3,5,2,3]
point1 = 0
point2 = 1

while point1 < len(nums):
      if point2 < len(nums):
            while point2 <= len(nums) - 1:
                  print([nums[point1],nums[point2]])
                  point2 +=1
      point1 +=1
      point2 =point1 + 1
                
    




