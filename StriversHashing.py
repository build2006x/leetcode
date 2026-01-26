##### while doing hashing in the list you have to check the key is been present or not only this case for the dict 
arr = [1,3,12,12,2]

freq = [0]  * 29

for i in arr:
    freq[i] +=1

print(freq[12])