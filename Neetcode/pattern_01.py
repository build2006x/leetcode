### hey hi today i am learning two new pattern 

nums = [1, 12, -5, -6, 50, 3]
k = 4

l = 1
r = k 
avg = 0
old_sum = sum(nums[0:k])
avg = old_sum//k

while r < len(nums):
      old_sum += old_sum - nums[l] + nums[r] 
      avg = max(avg,old_sum//4)
      r +=1
      l +=1

print(avg)