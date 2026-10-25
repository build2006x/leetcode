#### hey hi today i am working on the 5th easy practice sums on the sliding window pattern 

nums = [1, 2, 3, 4, 5]
k = 2
target = 7

l = 0
r=k
window_sum = sum(nums[0:k])
sum_val = window_sum
if sum_val >=target:
        count +=1
count = 0


while r < len(nums):
        window_sum = window_sum - nums[l] + nums[r]
        if window_sum >= target:
            count +=1
        l +=1
        r +=1

print(count)