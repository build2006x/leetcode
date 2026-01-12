### today i doing the 3rd pattern in the strivers dsa sheet
### the pattern goes like 
"""
    a
   aba
  abcba
 abcdcba

Docstring for leetcode.11-01-2026_striver-3
"""
space = 0
arr = ["A","B","C","D"]
result = ""

for i in range(1,6):
    space = (9-i)//2
    for j in range(0,i):
         print("" * space + str(arr[j]),end="")
    print("")

 