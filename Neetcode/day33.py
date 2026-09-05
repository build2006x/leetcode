### hey hi today i am working on the 
##Maximum Product Difference Between Two Pairs

"""
algorithm****
1.take one pair 
2.before compare with all other same pair would not be compared 
3.compute each pair of the sum and store in the array return the max one 
"""
nums = [5,6,2,7,4]

first = 0 
second =  first + 1
last = -1
last_before = -2 

nums_sorted = sorted(nums)

ans = (nums_sorted[last] * nums_sorted[last_before]) - (nums_sorted[first] * nums_sorted[second])

print(ans)