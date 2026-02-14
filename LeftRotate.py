### today i am working on the left rotate array by 1 

nums =  [-1, 0, 3, 6]  
first= nums[0]

for i in range(0,len(nums)-1):
     nums[i] = nums[i+1]
     if i == len(nums)-2:
          nums.pop()
          nums.append(first)

print(nums)