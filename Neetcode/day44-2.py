### hey hi  today i am working on the removing the duplicate from the array 
nums = [1,1,1,2,2,3]
pointer = 0
vaild = 0
count = 0
reader = 0 
res = []

for i in nums:
     if i not in res:
          res.append(i)

while pointer < len(res):
        while reader < len(nums):
            if res[pointer] == nums[reader]:
                    count +=1
                    nums[vaild] = nums[reader]
                    vaild +=1
                    if count == 2:
                            break
            reader +=1
        reader  = 0
        count = 0
        pointer +=1

