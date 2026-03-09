### hey hi da this leetcode sum is to find the most common words in the string not banned names 

para = paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.".lower().replace(".","")
banned = ["hit"]

arr = para.split(" ")

arrs = [0,3,2,4,4,25,24]
fre = {}

for i in arr:
    if i in fre and i !=banned:
        fre[i] +=1
    else:
        fre[i] = 1

print(fre)

# print(fre)
# max_idx = 0

# for val,idx in fre.items():
#     if val 


