### today i am sovling the leetcode problem - 1877 
# 1877. Minimize Maximum Pair Sum in Array
## the problem is finding the minimized maxium pair sum 

# num = sorted(nums)
# point1 = 0
# point2 = 1
# count = len(nums)//2
# result = []

# while point1 < len(nums):
#       if point2 < len(nums):
#             while point2 <= len(nums) - 1:
#                   result.append(nums[point1]+nums[point2])
#                   point2 +=1
#                   count -=1
#       point1 +=1
#       point2 =point1 + point1

# print(max(result))
####--- now we have the all the combination of the pairs of the nums array 
####--- now we have to filter out the pairs which satifies the condition 

### this problem is not just about finding the pairs of highest sums ---
nums = [3,5,4,2,4,6]
arr = sorted(nums)
point1 = 0
point2 = len(arr) - 1
count = len(arr)//2
result = []

while count !=0:
    result.append(nums[point1]+nums[point2])
    count -=1
    point1 +=1
    point2 -=1

print(max(result))


### the logic is nothing we gone to make that list of pair should be balancing to maintan so what gone to sort the array 
### and then we are making start point and last pointer making them to move forwards to each other 













