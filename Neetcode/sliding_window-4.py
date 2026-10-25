### hey hi today i am working on the silding window --4
nums = [1, 3, 2, 6, -1, 4]
k = 3


l = 0
r = k
window_sum = sum(nums[0:k])
avg = window_sum/k

while r < len(nums):
      window_sum = window_sum - nums[l] + nums[r]
      avg = max(avg,window_sum/k)
      l +=1
      r +=1

print(avg)