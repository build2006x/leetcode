## hey hi today i am praticing the silding window problem 

nums = [1, 2, 3, 4, 5]
k = 3

old_sum = sum(nums[0:k])
result = []
result.append(old_sum)
l = 0
r = k 

while r < len(nums):
    old_sum = old_sum - nums[l] + nums[r]
    result.append(old_sum) 
    l +=1
    r +=1

print(result)