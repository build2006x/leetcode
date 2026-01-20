### today i finishing the recursion in the strivers dsa sheet 
### recursion last topic - fibonacci number 
### finding the series up to n terms in the fibonacci series 

# def fibonaciSeries(N):
#     for i in range(0,N):
#         if (i + i+1) != (i+2):
#             print(i,i+1,end="")

# result = fibonaciSeries(N = 5)

#### brute force approach  to finding the fibonaci number or not
# def fibonaciNumber(N):
#     n1,n2 = 0,1
#     for i in range(N+1):
#         print(n1, end=" ")
#         n1 , n2 = n2 , n1 + n2 

# fibonaciNumber(6)

##sturture of the recursion function 
###  
### 1.main function calling 
### 2.base case for failing occurs 
### 3.recursive calls 
# def fibonacciSeries(N,n1,n2):
#     if N == 0:
#         return ""
#     print(n1,end=" ")
#     return fibonacciSeries(N-1,n1=n2,n2=n1+n2)
# result = fibonacciSeries(N=5+1,n1=0,n2=1)
# print(result)

### i am now trying to do with thinking in the brute force 

n1,n2 = 0,1
n = 5
for i in range(0,n+1):
    print(n1)
    n1,n2 = n2,n1+n2


