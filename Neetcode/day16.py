### hey hi today i working on the finding the strictly inc or des 

nums = [1,4,3,3,2]

l = 0
r = 1
start = 0
reader = 1
result = []

while r < len(nums):
    print(nums[l],nums[r])
    if nums[l] > nums[r] and nums[l] != nums[r]:
        start = l
        reader +=1
        l +=1
        r +=1
    else:
        result.append(nums[l:r+1])
        l +=1
        r +=1
        start = 0
        reader = 1


# l = 0
# r = 1
# start = 0
# reader = 1

# while r < len(nums):
#     if nums[l] < nums[r]:
#         start = l 
#         reader +=1
#         l +=1
#         r +=1
#     else:
#         result.append(nums[l:r+1])
#         l +=1
#         r +=1
#         start = 0
#         reader = 1

print(result)


