### today i encountering the second recursion second of n to 1 times
### reversing the previous question 


def recursion(n,count):
       if n==0:
              return ""
       print(count,end=", ")
       return recursion(n-1,count-1)


result = recursion(n=4,count=4)
