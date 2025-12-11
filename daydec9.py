#understading the two pointer for doing the 3sum 

nums = [2, 7, 11, 15]	

left = 0
right  = len(nums) - 1
target = 9

while left<right:
      if nums[left] + nums[right] == target:
            print([left,right])
      elif nums[right] + nums[right] > target:
            right -=1
      else:
            left -=1

