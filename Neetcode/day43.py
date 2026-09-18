#### hey hi this is barath kumar --today i am working on the 
#### 2109. Adding Spaces to a String

# s = "LeetcodeHelpsMeLearn"
# spaces = [8,13,15]

# space = sorted(spaces)
# s_t = list(s)

# pointer = 0
# reader = 0
# result = ""
# p = 0

# while pointer < len(space):
#      s_t.insert(space[pointer]+p, " ")
#      p +=1
#      pointer +=1

# s = "".join(s_t)

# print(s)


# (above_my logic)



pointer = 0
reader = 0
result = []
s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]


while pointer < len(s):
     if  reader < len(spaces) and pointer == spaces[reader]: 
                    result.append(" ")
                    reader +=1
     result.append(s[pointer])
     pointer +=1

s = "".join(result)

print(s)