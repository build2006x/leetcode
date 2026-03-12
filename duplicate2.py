#### this is approach  using the brute force to solve the problem 

# def findDupe(nums,k):
#     for i in range(0,len(nums)):
#        for j in range(i+1,len(nums)):
#            if nums[i] == nums[j] and abs(i-j) <=k:
#                return True
#     return False
# result = findDupe([1,2,3,1,2,3], k = 2)
# print(result)

##### this could be can you solved using the window sliding  window

### like we can use the approach of the sliding window 

def findDupe(nums,k):
    left = 0
    rigth = 2
    while left < len(nums) - 1:
        sumVal =rigth - left
        if nums[left] == sumVal:
            if abs(left + rigth) <= k:
                return True
        sumVal = 0
        rigth +=1
        left +=1
    return False     
 
result = findDupe( nums = [1,0,1,1], k = 1)

print(result)