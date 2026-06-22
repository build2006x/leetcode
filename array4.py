### hi today i am working on the 3sum problem 
##3sum question is focusing on the finding the pairs of array where sum equals to  0 

nums = [-1, 0, 1, 2, -1, -4]

pointer_one = 0
pointer_two = 1
pointer_three = 2


count = 4
while count != 0 :
    if nums[pointer_one] + nums[pointer_two] + nums[pointer_three] == 0:
        print([pointer_one,pointer_two,pointer_three])
    pointer_one +=1
    pointer_three +=1
    pointer_two +=1
    count -=1    
            


        




