### hi today i am working on the 3sum problem 
##3sum question is focusing on the finding the pairs of array where sum equals to  0 

nums = [-1, 0, 1, 2, -1, -4]

fixed = 0
left = fixed + 1
right = 2


while fixed != 4:
    while right < len(nums):
          if nums[fixed] + nums[left] + nums[right] == 0:
                print([nums[fixed],nums[left],nums[right]])
          right +=1
          left +=1
    fixed +=1
    left = fixed + 1
    right = left + 1

 


            


        




