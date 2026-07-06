### today i am working on the neetcode day 8 strike --> 
from collections import Counter


nums = [5,5,1,1,1,5,5]
val = 0
count = Counter(nums)

for i in count.values():
       val = max(val,i)

for i,j in count.items():
      if j == val:
             print(i)
             