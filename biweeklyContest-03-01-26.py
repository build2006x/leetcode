####today i am working on the biweekly contest 

s = "abcd"

string = list(s)

k = 2 - 1

start = 0

while start <= k :

      string[start],string[k] = string[k],string[start]
      start +=1
      k -=1

result = "".join(string)
print(result)