### today i am working on the sum 
### 1968. Array With Elements Not Equal to Average of Neighbors
nums = [1,3,2]
l = 0
r = len(nums) - 1
n = sorted(nums)
res = []

while l != r:
     res.append(n[l])
     res.append(nums[r])
     l +=1
     r -=1

while l<=r:
     res.append(nums[l])
     l +=1

print(res)