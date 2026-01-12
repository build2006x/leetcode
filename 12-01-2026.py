##today strivers
## check the give numbers is armstrong or not 

n = 12
power = len(str(n))
result  = 0

for i in str(n):
    result += pow(int(i),power)

print(result)