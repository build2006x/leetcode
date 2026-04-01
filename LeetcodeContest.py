#### this would be the sum
#### of finding the first matching pairs to be do

s = "abcacbd"
left = 0

right = len(s) - 1
arr = []

while left < right:
     if s[left] == s[right]:
          print(left,right)
     left +=1
     right -=1
