### today i finishing the recursion in the strivers dsa sheet 
### recursion last topic - fibonacci number 
N = 5

#### brute force approach 
def fibonaciNumber(N):
    for i in range(0,N):
        if (i + i+1) != (i+2):
            return False
    return True 

result = fibonaciNumber(N = 5)
print(result)


