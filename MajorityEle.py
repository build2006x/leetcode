###this problem is about finding the majority element in the array 

freq = {}

nums = [2,2,1,1,1,2,2]

for i in nums:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1

lenght = len(freq)
val_idx  = 0

max_key = max(freq, key=lambda k: freq[k])
print(max_key) 