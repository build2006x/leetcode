### hey hi today i am working on the problem rearrange according to the postive and negative in the order 

arr = [1,2,-4,-5]

p = []
n = []

for i in arr:
    if i < 0:
        n.append(i)
    else:
        p.append(i)

result = []

for i in range(0,len(arr)):
    if i < len(p):
      result.append(p[i])
    if  i < len(n):
      result.append(n[i])

print(result)