#### hey hi this is barath kumar --today i am working on the 
#### 2109. Adding Spaces to a String

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

space = sorted(spaces)
s_t = list(s)

pointer = 0
reader = 0
result = ""

while pointer < len(s):
     if space[reader] == pointer and reader == 0:
          s_t.insert(space[reader] + 1 ," ")
          reader +=1 
     elif reader == pointer and reader > 1:
          s_t.insert(space[reader]+1," ")
          reader +=1
     pointer +=1

s = "".join(s_t)

print(s)
