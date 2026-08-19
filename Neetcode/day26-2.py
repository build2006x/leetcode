### Find Lucky Integer in an Array

### this is the problem right now i am working on 
from collections import Counter

arr = arr=[2,2,3,4]
count = 0
ar = Counter(arr)

for fre,val in ar.items():
    if fre == val:
        print(val)

