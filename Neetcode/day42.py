# 2460. Apply Operations to an Array
nums = [1,2,2,1,1,0]
l =  0 
r =  1

while r < len(nums):
        if nums[l] == nums[r]:
                    nums[l] =    nums[l] * 2 
                    nums[r] = 0
        l +=1
        r +=1
        
p = 0
pointer = 0

print(nums)
while pointer < len(nums):
        if nums[pointer] != 0:
                nums[p] = nums[pointer]
                p +=1
        pointer +=1

for i in range(p,len(nums)):
        nums[i] = 0

print(nums)