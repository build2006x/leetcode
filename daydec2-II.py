#sums info like i have to find the the jump steps are being
#help us to move to the last means we have to send true 
#orelse false 

#what logic i think in my mind is like
#keeping a pointer varible move them 
#reasign the variable to the pointer and check with like steps == len(nums) - 1: len(nums) is real index of the nums 
#our focus the jumping is can reach the position towards the last index 

nums = [2,3,1,1,4]
p1 = 0

def canJump(nums,p1):
    steps = p1
    while True:
        p1 = nums[p1]
        steps = max(steps,p1)
        if steps > len(nums) - 1: 
            return False
        elif nums[steps] == 0:
            return False
        elif steps == len(nums)-1:
            return True
        else:
            p1 +=1 

result = canJump(nums,p1)
print(result)