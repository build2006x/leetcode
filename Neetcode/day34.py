### hello all i am working on the Maximum Score After Splitting a String
from collections import Counter
s = "011101"




left = 0
right = 1
score = []
mark = 0

while left < len(s)-1:
        zero_count = Counter(s[:left+1])
        one_count = Counter(s[right:]) 
        mark = zero_count['0'] + one_count['1']
        print(zero_count['0'],one_count['1'])
        score.append(mark)
        mark = 0
        left +=1
        right +=1
        zero_count = 0
        one_count = 0


print(max(score))
