### hey hi today i am working on the 3 sum question leetcode

nums =  [-2,0,0,2,2]
result = []
pointer = 0
l = 0
r = 1


while pointer < len(nums):
        while r < len(nums):
                if l != pointer and pointer != r and l != r and  nums[l] + nums[r] + nums[pointer] == 0 and sorted([nums[pointer],nums[l],nums[r]]) not in result:
                              print(pointer,l,r)
                              result.append(sorted([nums[pointer],nums[l],nums[r]]))
                l +=1
                r +=1
        r = 1
        l = 0
        pointer +=1

print(result)