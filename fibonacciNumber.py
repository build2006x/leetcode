### today i finishing the recursion in the strivers dsa sheet 
### recursion last topic - fibonacci number 
### finding the series up to n terms in the fibonacci series 

# def fibonaciSeries(N):
#     for i in range(0,N):
#         if (i + i+1) != (i+2):
#             print(i,i+1,end="")

# result = fibonaciSeries(N = 5)

#### brute force approach  to finding the fibonaci number or not
def fibonaciNumber(N):
    n1,n2 = 0,1
    for i in range(N+1):
        print(n1, end=" ")
        n1 , n2 = n2 , n1 + n2 

fibonaciNumber(6)



