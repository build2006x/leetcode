### strviers easy question to workout 

n = 123

string = str(n)

print(str(n)==string[::-1])


###finding the gcd sum in the strivers easy question get started

n1 = 4 
n2 = 6

result  = []

for i in range(1,n1*n2):
    if n1%i == 0 and n2%i ==0:
          result.append(i)


print(max(result))
