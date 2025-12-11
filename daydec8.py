#3sum 

##like finding of the sum of three number == 0 

# Input = [-1,0,1,2,-1,-4]
     
#like my approach like keeping the two pointer in the last element in array and first pointer to first element 
#like keeping the first pointer as dyanamic moving the pointer and keeping the last two as static 
# Input = list(set(Input))
# p1 = 0
# p2  = len(Input) - 2
# p3 = len(Input) - 1
# final = []

# while p2 < p1:
#      if Input[p1]+Input[p2]+Input[p3] == 0:
#           final.append([Input[p1],Input[p2],Input[p3]])
#      p2 -=1
#      p3 -=1


# print(final)
          


def twoSum():
    nums = [2, 7, 11, 15]
    p1 = 0 
    p2 = len(nums) - 1
    target = 9
    while p2 < p1:
        if nums[p1] + nums[p2] == target:
            print(p1,p2)
        p2 -=1
        
    print('cant find')
      

twoSum()