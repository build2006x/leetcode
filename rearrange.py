### hey hi today i am working on the problem rearrange according to the postive and negative in the order 

arr = [3,1,-2,-5,2,-4]

p = []
n = []

for i in arr:
    if i < 0:
        n.append(i)
    else:
        p.append(i)

result = []
read = 0

for i in range(0,len(arr)):
    if i < len(p):
      arr[read] = p[i]
      read +=1
    if  i < len(n):
      arr[read] = n[i]
      read +=1

print(arr)

### let us think in the two pointer method to avoid the extra  memory useage 
