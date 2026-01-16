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
### brute force appraoch for the plaindrome string 

# string = "TAKE U FORWARD"
# new_string = ""
# end = len(string) - 1

# for i in range(0,len(string)):
#        new_string = new_string + string[end]
#        end -=1

# if string == new_string:
#        print('plaindrome')
# else:
#        print('not a plaindrome')
             
### using the optimal ways of solving this problem 
### using the recursion techinique i am going to solve this problem

### this is a techinque for checking the palindrome

def recursion_plaindrome(string,start,end):
       if string[start] != string[end]:
                  return print("False")  ### this condition is for invaild string 
       elif start == end:
                  return print('True')  ### checking that like if the pointer both reach the center means true 
       else:
             recursion_plaindrome(string,start+1,end-1) ### if not both call again until hit any one condition 

recursion_plaindrome(string="TAKE U FORWARD",start=0,end=len(string)-1)
