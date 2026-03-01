### 
s = "day"
strinput = s[::-1]
arr =  ['a', 'e', 'i', 'o','u']

for idx,char in enumerate(strinput):
    if char not in arr:
         break

print(strinput[idx:][::-1])
