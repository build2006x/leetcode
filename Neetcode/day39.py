### today i am putting a game 

s="aca"
pointer = 0

chars = list(s)

print(chars == chars[::-1])


while pointer < len(s):
    s = s[:pointer] + s[pointer+1:]
    if s[::-1] == s:
        print('yes')
    pointer +=1
 