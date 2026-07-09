### today i am working on the pascal triangle problem 
nums = [0,1,2,2,3,0,4,2]
val = 2

pos  = 0
pointer = 0

real_len = len(nums)

while pointer < len(nums):
      if nums[pointer] != val:
            nums[pos] = nums[pointer]
            pos +=1
      pointer +=1

for i in range(pos,len(nums)):
       nums[i] = 0
       real_len -=1

print(real_len)
