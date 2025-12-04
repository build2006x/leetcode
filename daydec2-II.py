#sums info like i have to find the the jump steps are being
#help us to move to the last means we have to send true 
#orelse false 

#what logic i think in my mind is like
#keeping a pointer varible move them 
#reasign the variable to the pointer and check with like steps == len(nums) - 1: len(nums) is real index of the nums 
#our focus the jumping is can reach the position towards the last index 



#today i worked on the solution of the jump sum still i will solve soon 

def jump_game():
    nums = [2,3,0,1,4]
    left_step = nums[0]
    for i in range(len(nums)):
       left_step -=1
       if i < 0:
           return False
       elif i == len(nums) - 1:
           return True
       left_step = max(left_step,nums[i])


result = jump_game()


print(result)