### nums = [2, 7, 11, 15], target = 9


## today i was trying to learn two and 3 sum brute force thinking how to think in the two pointer also 


# nums = [3, 2, 4]
# target = 6


# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] == target:
#             print([nums[i],nums[j]])



### now let me try to turn this into two pointer approach ---like i need to do the binnary search if the array is sorted means i will do 
### right now its being un sorted so we need to in place see and give it out


# pointer = 0
# reader = pointer + 1

# while pointer < len(nums):
#     while reader < len(nums):
#         if nums[pointer]+nums[reader] == target and pointer != reader:
#              print([nums[pointer],nums[reader]])
#         reader +=1
#     pointer +=1
#     reader = 0 


### now i am going to write the optimal soultion of the 2 sum problem 

nums = [3, 2, 4]
target = 6

result = {}

for idx,val in enumerate(nums):
        com = target - val
        if com in result:
            print([result[com],idx])
        result[val] = idx


### how you can understand this means by you minus the number remaining would be if there loop is there return and orelse store them in the hashmap 
