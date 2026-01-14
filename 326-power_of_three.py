##today i working on the power of three

# def isPowerOfThree(n):
#     return n > 0 and 1162261467 % n == 0

# result = isPowerOfThree(27)

# print(result)


### for learning the recursion function like 

### three cases are there 

#1.base case
#2.smaller the problem
#3.recursive calls for continous calls

# def factorial(n): 
#     if n == 0:
#      return 1 
#     return n * factorial(n - 1) 
        
# result = factorial(5)
# print(result)
# base case# recursive case

###from the above learning i am trying to solve the sums in the power of three
###

def power_of_three(n):
    if n == 1:
        return True
    elif n % 3 != 0 or n < 0:
        return False
    return power_of_three(n//3)
 

result = power_of_three(n=27)
print(result)