### strivers dsa following the easy sums to get started with leetcode 
### finding the prime number 

n = 4
click  = 0 
count = 0

for i in range(2,n):
    if n%i == 0 :
        count +=1

if count > 0:
    print('not prime')
else:
    print("prime number")



