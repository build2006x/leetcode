### hey hi today i am working on the 3 sum question leetcode

nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]
# result = []
# stack1 = 0
# stack2 = 1
# die = stack2 + 1


# while stack2 < len(nums):
#         while die < len(nums):
#                 if die != stack2  and die != stack1 and  nums[stack1]+nums[stack2]+nums[die] == 0 and sorted([nums[stack1],nums[stack2],nums[die]]) not in result:
#                                         result.append(sorted([nums[stack1],nums[stack2],nums[die]]))
#                                         die +=1
#                 else:
#                         die +=1
#         stack1 +=1
#         stack2 = stack1 + 1 
#         die = 0 

result = set()
count = 0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
         for k in range(j+1,len(nums)):
               if nums[i]+nums[j]+nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                

print(result)
print(count)


### the good thing i learnt so far about the far whenever i am facing the index duplicate problem i will think to go for the for loop 
### becuase the poitner appraoch needs to thinking more of the reseting correctly the variabel values 

### i will go for the for loop only if the constrain are the less where the for loop will be working fine well 

