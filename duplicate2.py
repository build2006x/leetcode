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
    return ""
result = findDupe(nums = [1,0,1,1], k = 1)

print(result)