### hey hi today i am working on the Number of Good Pairs 


nums = [1,2,3,1,1,3]
main_pointer = 0
p1 = 0
p2 = 1

while main_pointer < len(nums):
        while p2 < len(nums):
            if nums[p1] == nums[p2] and p1 < p2:
                print(p1,p2)
            p2 +=1
        p1 +=1
        p2 = p1 + 1
        main_pointer +=1