############## hey hi today i am working on the 
nums=[1,2,3,4,5,6,7]
k=3

k_val = k % len(nums)

r = -k

p1 = 0
l = 0

while p1 < k:
     nums[r],nums[l] = nums[l],nums[r]
     r +=1
     l +=1
     p1 +=1

print(nums)
