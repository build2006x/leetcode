### hey hi today i am working on the sliding window problem 
from collections import Counter
blocks="BBBBBWWWWBWBWBWBWWWBWBWBBBWBBBBW"
k=14


min_w = 0
count = Counter(blocks[0:k])
min_w += count['W']
l = 1
r = k

while r < len(blocks):
            s = Counter(blocks[l:r+1])
            if s['B'] == k:
                     min_w = 0
                     break
            elif l == 'W':
                    min_w -=1
            elif r == 'W':
                  min_w +=1
            l +=1
            r +=1

print(min_w)