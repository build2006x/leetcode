#this sum is like appling the operation on a array 

##
nums = [1,2,2,1,1,0]

 
point1 = 0
point2 = 1
endPoint = len(nums) - 1

result = []

while point2 != len(nums) - 1:
      if nums[point1] == nums[point2]:
             nums[point1] *=2
             nums[point2] = 0
             nums[point2],nums[endPoint] = nums[endPoint],nums[point2]
             point1 +=1
             point2 +=1
      elif nums[point1] != nums[point2]:
           point2 +=1
           point1 +=1
count = 0
for num in nums:
      if num != 0:
            result.append(num)
      else:
            count +=1

while count  > 0:
      result.append(0)
      count -=1

print(nums)
print(result)

###i work on this like i am knowing the logic 