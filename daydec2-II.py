#sums info like i have to find the the jump steps are being
#help us to move to the last means we have to send true 
#orelse false 


def canJump():
    nums = [2,3,1,1,4]
    p1 = 0
    while p1 < len(nums) -1:
            p1  = nums[p1]
            if p1 > len(nums) - 1:
                return False  
            elif nums[p1] ==0:
                return False
            elif p1 == len(nums) - 1:
                return True
            else:
                p1 +=1 


result = canJump()
print(result)