### hey hi today i am working on the sliding window problem --> 

# l = 0 
# r = 0
# pointer = 1
# res = []


# while pointer < len(nums):
#         while r < len(nums):
#                 if sum(nums[l:r+1]) == target:
#                             print(nums[l:r+1])
#                 r +=1
#                 l +=1
#         l = 0 
#         r = pointer 
#         pointer +=1

### above logic is all about the brute force --> 

### hey hi above code is run on the o(n2) time complexity where i wanted to change into the o(1)

target = 7
nums = [2, 3, 1, 2, 4, 3]
k = 2
l = 0 
r = 1

old_sum = sum(nums[l:k])

res = []

if old_sum >= target:
      res.append(len(nums[l:r+1]))

while r < len(nums):
        old_sum = old_sum - nums[l] + nums[r]
        print(old_sum)
        if old_sum >=target:
              res.append(len(nums[l:r]))
        r +=1
        l +=1

