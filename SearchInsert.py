# seraching the insert position 
nums = [1,3,5,6] 
target = 2

# for i in range(0,len(nums)):
#     if nums[i] == target:
#         print(i)

for i in range(0,len(nums)):
     if target < nums[i]:
          print(i)
          break