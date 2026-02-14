### today i working on the k position of the array as 
### i encounter the rotate the by 1 position array element...

###### --- 
nums = [1, 2, 3, 4, 5, 6]
k = 2

### simple brute force we can think is to append the after the 
###  k element in the list first and then remaining
result = []
for i in range(k,len(nums)):
    result.append(nums[i])

for i in range(0,k):
    result.append(nums[i])

print(result)