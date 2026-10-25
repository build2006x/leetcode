### hey hi today i am working sliding window pratice of easy problem --3 

nums = [4, 2, 1, 7, 3, 2]
k = 2

l = 0
r = k
window = sum(nums[0:2])
win_sum = window

while r < len(nums):
      window = window - nums[l] + nums[r]
      win_sum = min(win_sum,window)
      l +=1 
      r +=1

print(win_sum) 