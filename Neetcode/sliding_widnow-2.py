#### hey hi today i am working on the Practice 2 — Maximum sum of a window
nums = [2, 1, 5, 1, 3, 2]
k = 3

sum_val = sum(nums[0:k])
res = sum_val
l = 0
r = k

while r < len(nums):
       sum_val = sum_val - nums[l] + nums[r]
       res = max(res,sum_val)
       l +=1
       r +=1

print(res)
