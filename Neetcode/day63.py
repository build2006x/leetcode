### hey hi today i am working on the binnary search of the medium level problem 

nums = [1,2,3]


count = 0 
big = len(nums)-1
reader = 0
take = 0

while len(set(nums)) != 1:
    reader = 0 
    take =big
    while reader < len(nums):
        if nums[reader] == nums[big] and reader != big:
                nums[reader] += 1
                take = reader
        elif reader != big:
            nums[reader] += 1
        reader +=1
    big = take
    count +=1

print(count)