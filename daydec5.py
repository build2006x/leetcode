##jump game 
## 

#logic having a variable 

#Like today i have a overview of this jump not indepth understanding of this sum 

#like what they are doing like they have a variable step 

#variables step = nums[o]
def find_reach():
        nums = [3,2,1,0,4]
        steps = nums[0]
        for i in range(len(nums)):
            #here each i is like the index over the array 
            #steps will decrease for the each move over the next element 
            steps -=1
            if steps < 0:
                return False
            elif nums[i] + i == len(nums) - 1:
                return True
            elif steps < nums[i]:
                steps = nums[i]


result = find_reach()

print(result)