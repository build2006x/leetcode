### Check if Array Is Sorted and Rotated today i am working on this problem 
### the problem defintion is that i need check the array is non desecending order if not i need to use the formula to shift the array for every vaild index 
### no shift cant be equal to the sorted array means return False 


nums = [2,1]
pointer = 0
roated_arr = []

if sorted(nums) == nums:
    print('true')


while pointer < len(nums):
   if sorted(nums) == roated_arr:
      print('True')
      break
   else:
        roated_arr = nums[pointer:] + nums[:pointer]
        pointer +=1

