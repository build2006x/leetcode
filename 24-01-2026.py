### today i am sovling the leetcode problem - 1877 
# 1877. Minimize Maximum Pair Sum in Array
## the problem is finding the minimized maxium pair sum 

nums = [3,5,2,3]
num = sorted(nums)
point1 = 0
point2 = 1
count = len(nums)//2
result = []

while point1 < len(nums):
      if point2 < len(nums):
            while point2 <= len(nums) - 1:
                  result.append(nums[point1]+nums[point2])
                  point2 +=1
                  count -=1
      point1 +=1
      point2 =point1 + point1

print(max(result))
####--- now we have the all the combination of the pairs of the nums array 
####--- now we have to filter out the pairs which satifies the condition 



