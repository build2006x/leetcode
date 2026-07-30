### hey today i am working on the pivot index finding problem 
### there is another constrain like if the pointer is at the left edge of the array means we will be left sum is zero 

nums =[-9,9,2]

index = len(nums) -1
result = 0
res = -1

while index !=-1:
        if sum(nums[:index]) == sum(nums[index+1:]):
                 result = index
                 index -=1
        else:
             index -=1

if result == 0:
        if 0 == sum(nums[index+1:]):
             print(0)
        else:
               print(-1)
else:
     print(result)

