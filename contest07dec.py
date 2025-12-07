#today a easy sum 
#i like sort the array based on the binnary reflection 


#steps in mind to solve this problem 

# 1 find the reflection of the binnary of each number in the array

nums = [3,6,5,8]
digits = 0

for i in range(len(nums)):
    #this will change the number into binnary 
    digits = format(i,'b')
    #this is will make the string to reverse
    digits = digits[::-1]
    nums[i] = digits
    digits = 0






