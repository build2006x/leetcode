### today i am working on the sum 
### 1968. Array With Elements Not Equal to Average of Neighbors

nums = [1,3,5,7]
c = 1 
l = c - 1 
r  = c + 1
s = 0

if len(nums) == 3:
            nums[l],nums[c] = nums[c],nums[l]

while c < len(nums) - 2:
        if (nums[l]+nums[r])/2 == nums[c]:
                    s = r 
                    while s < len(nums) -2:
                        nums[s],nums[s+1] = nums[s+1],nums[s]
                        s +=1
        else:
            c +=1
            l +=1 
            r +=1


print(nums)