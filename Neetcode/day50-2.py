####
#### hey hi today i am working on the 4sum problem

nums = [3,2,3,-3,1,0]
target = 3
result = []

arr = sorted(nums)
###[-3, 0, 1, 2, 3, 3]

p1 = 0
p2 = p1 + 1
l = p2 + 1
r = len(nums) -1 

while p2 <len(nums)-2:
        while nums[p1] > 0:
            p1 +=1
            p2 = p1 + 1
            continue  

        while l < r:
                if nums[p1]+nums[p2]+nums[l]+nums[r] == target:
                            result.append([nums[p1],nums[p2],nums[l],nums[r]])
                            l +=1
                            r -=1
                elif  nums[p1]+nums[p2]+nums[l]+nums[r] < target:
                         l +=1
                else:
                         r -=1  

print(result)                       