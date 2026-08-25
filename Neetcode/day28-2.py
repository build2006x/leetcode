### hey hi Divide Array Into Equal Pairs 

from collections import Counter

nums = [1,2,3,4]
n_len = Counter(nums)

for i in n_len.keys():
    if i % 2 != 0:
        print('Flase')

