### plaindrome sums 
### trying to solve this in three ways of twpointer inplace and brute force and inbuilt 
### python function 


### inbuilt function

def plaindrome(string):
     return string[::-1] == string

result = plaindrome(string="TAKE U FORWARD")
print(result)
