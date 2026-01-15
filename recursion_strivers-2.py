### today i am doing the second
### recursion call structure 

## base function 
## recursive call 

def recursion(n,count):
    if n == 0:
        return ""
    print(count,end=",")
    return recursion(n-1,count+1)

result = recursion(n=4,count=1)
print()