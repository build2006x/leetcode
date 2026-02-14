### today i am working on the left rotate array by 1 

# nums =  [-1, 0, 3, 6]  
# first= nums[0]

# for i in range(0,len(nums)-1):
#      nums[i] = nums[i+1]
#      if i == len(nums)-2:
#           nums.pop()
#           nums.append(first)

# print(nums)


### anothor brute force 
# nums =  [-1, 0, 3, 6]  
# result = []

# for i in range(1,len(nums)):
#       result.append(nums[i])
# result.append(nums[0])
# print(result)


#### this is the brute force method above now we explore the 
#### the main optimal way of doing above problem 

