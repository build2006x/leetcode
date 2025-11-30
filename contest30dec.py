nums = [3,1,2]
k = 1
nums[:] = sorted(nums)
p1 = 0
count = 0
qualified = 0

while p1 < len(nums) - 1:
      p2 = p1 + 1
      while p2 <= len(nums) - 1:
            if nums[p1] > nums[p2]:
                  qualified +=1
                  if qualified >= k:
                        count +=1
                        break

      qualified=0
      p1 +=1 
                  

print(count)
