### hey hi da this leetcode sum is to find the most common words in the string not banned names 
import re



paragraph = paragraph = "Bob hit a ball, the hit BALL flew far after it was hit".lower()
para = re.sub(r"[.,]", " ",paragraph)
banned = ["hit"]
arr = para.split(" ")
fre = {}

for i in arr:
    if i and i not in banned:
        if i in fre:
            fre[i] +=1
        else:
            fre[i] =1

max_val = 0
length = len(fre)

for key,val in fre.items():
    max_val = max(max_val,val)
    if length == 1:
       for key,val in fre.items():
           if max_val == val:
               print(key)
    length -=1


### algorithm for this question to solve by 
### first make the string into lowercase
### finding the count of the all string 
