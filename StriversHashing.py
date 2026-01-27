##### while doing hashing in the list you have to check the key is been present or not only this case for the dict 
# arr = [1,3,12,12,2]

# freq = [0]  * 29

# for i in arr:
#     freq[i] +=1

# print(freq[12])


### finding the highest and lowest frequecny of the element 

arr = [10,5,10,15,10,5]
freq = {}
result = []


for i in arr:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1

max_freq = max(freq.values())
min_freq = min(freq.values())

for key,val in freq.items():
    if max_freq == val:
            print(f"Max {key} : {max_freq}")
    elif min_freq == val:
            print(f"Min {key} : {min_freq}")

