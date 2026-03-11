
def findDupe(nums,k):
    for i in nums:
       if nums[i] == nums[i+1] and abs(i-i+1) <=k:
                return True
    return False

result = findDupe(nums = [1,0,1,1], k = 1)
print(result)