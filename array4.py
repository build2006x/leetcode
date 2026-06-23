### hi today i am working on the 3sum problem 
##3sum question is focusing on the finding the pairs of array where sum equals to  0 

nums  = [-100,-70,-60,110,120,130,160]

nums.sort()

print(nums)

fixed = 0
left = fixed + 1
right = 2
result = []

while fixed != 4:
    while right < len(nums):
          if nums[fixed] + nums[left] + nums[right] == 0:
                if [nums[fixed],nums[right],nums[left]] not in result:
                     result.append([nums[fixed],nums[left],nums[right]])
          right +=1
          left +=1
          print(nums[fixed],nums[left],nums[right])
    fixed +=1
    left = fixed + 1
    right = left + 1
    break

print(result)

            


        




