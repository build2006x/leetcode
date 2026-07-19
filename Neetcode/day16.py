### hey hi today i working on the finding the strictly inc or des 

nums = [1,4,3,3,2]

l = 0
r = 1
start = 0
end = 0
result = []

while r < len(nums):
        if nums[l] > nums[r]:
            start = l
            end = l + 1
            r +=1
            l +=1
        else:
             result.append(nums[start:end+1])  
             l +=1
             r +=1
             start = 0
             end = 0

left = 0
right = 1
starting = 0
ending = 0

# while right < len(nums):
#         if nums[left] > nums[right]:
#             starting = l - 1 
#             ending = starting + 1
#             r +=1
#             l +=1
#         else:
#              result.append(nums[starting:ending+1])  
#              l +=1
#              r +=1
#              satrt = 0
#              end = 0
print(result)








