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

string = "TAKE U FORWARD"
new_string = ""
end = len(string) - 1

for i in range(0,len(string)):
       new_string = new_string + string[end]
       end -=1

if string == new_string:
       print('plaindrome')
else:
       print('not a plaindrome')
             
### using the optimal ways of solving this problem 
### using the recursion techinique i am going to solve this problem

def recursion(string,start,end):
       if string[Start] == string[end]:


result = recursion(string="ABCDCBA",Start=0,end=-1)
print(result)


