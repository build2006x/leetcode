### hey hi da this leetcode sum is to find the most common words in the string not banned names 

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
banned = ["hit"]
arr = paragraph.split(" ")


arrs = [0,3,2,4,4,25,24]

fre = {}

for i in arrs:
    if i in fre:
        fre[i] +=1
    else:
        fre[i] = 1


    