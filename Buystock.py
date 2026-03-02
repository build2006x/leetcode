#### today i working on the buy and sell the stock at the low prices 

nums = [7,6,4,3,1]

n = min(nums)
idx = nums.index(n)

max_value = 0

for i in range(idx,len(nums)):
    max_value = max(max_value,nums[i])


print(max_value-n)

