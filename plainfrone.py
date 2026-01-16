### plaindrome sums 
### trying to solve this in three ways of twpointer inplace and brute force and inbuilt 
### python function 


### inbuilt function

def plaindrome(string):
     return string[::-1] == string

result = plaindrome(string="TAKE U FORWARD")


### inplace two pointer approach 
string = "ABCDCBA"


def plaindromePointer():
        start = 0
        end = len(string)-1
        while start != end:
            if string[start] == string[start]:
                     start +=1
                     end -=1
            else:
                   return False 
        return True

result = plaindrome(string="TAKE U FORWARD")
print(result)
