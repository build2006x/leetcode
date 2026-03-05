### i am working on the sum which have to remove the the front  the remaining values
nums = [3,3]
val = 3
read = 0

for i in range(0,len(nums)):
    if nums[i] != val:
        nums[read] = nums[i]
        read +=1

print(nums[0:read])
        
