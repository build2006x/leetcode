###this problem is about finding the majority element in the array 

freq = {}

nums = [2,2,1,1,1,2,2]

for i in nums:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1

lenght = len(freq)
val_idx = 0

for val,idx in freq.items():
    val_idx = max(val_idx,idx) 

print(freq.items)