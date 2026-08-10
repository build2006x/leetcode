### Word Pattern
### there is  two condition ---> 
### two letter cant have equals to the same words 
### each letter have unique letter to words 

pattern = "abba"
s = "dog cat cat fish"

arr = s.split()
result = {}
checker = set()
count = 0

for idx,i in enumerate(pattern):
        if i in result:
            if  result[i] != arr[idx]:
                   print('false')
        else:
             if arr[idx] in checker:
                   print('False')
                   break
             result[i] = arr[idx]
             checker.add(arr[idx]) 


         
