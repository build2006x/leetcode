#### today i working on the sum where i need to find the number which have 1 count 

from collections import Counter

arr = [2,2,1]

Count = Counter(arr)

for i,j in Count.items():
    if j == 1:
        print(i)

#### here we are using the frequency module to get the count of the each element