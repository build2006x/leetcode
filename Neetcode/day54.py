### hey hi today i am working on the finding the subsquence of the pairs in the array 


nums = [3,5,6,7]
target = 9
res = []

reader = 0
pointer = 0

while pointer < len(nums):
        while reader < len(nums):
                if nums[reader]+nums[pointer] <= target:
                         print(nums[reader],nums[pointer])
                reader +=1
        reader = 0
        pointer +=1

    