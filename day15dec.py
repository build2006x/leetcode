nums = [1,2,2,1,1,0]

p1 = 0
p2 = p1 + 1

while p2 < len(nums):
    if nums[p1] == nums[p2]:
        nums[p1] *=2
        nums[p2] = 0
    p1+=1
    p2 +=1

pos = 0
for i in nums:
    if i !=0:
        nums[pos] = i
        pos +=1
        
while pos < len(nums):
    nums[pos] = 0
    pos +=1

print(nums)
