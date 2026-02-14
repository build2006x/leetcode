#### today i working on the moving the zero to the end leetcode sum 
nums = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]


### first let me done with brute force 
result = []
count = 0
for i in range(0,len(nums)):
    if nums[i] != 0:
        result.append(nums[i])
    elif nums[i] == 0:
        count +=1

for j in range(0,count):
    result.append(0)

print(result)