## today i working on to finish the recursion topics in the strivers sheet 
## factorial sums in the strivers sheet 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

result = factorial(n=3)
print(result)
