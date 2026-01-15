## today i working on to finish the recursion topics in the strivers sheet 
## factorial sums in the strivers sheet 

def factorial(n,result):
    if n == 0:
        return n
    return result * factorial(n-1,result=0)

result = factorial(n=5,result=0)
print(result)
