#solving before the sum of reserve the string - !!! sum i need to know how 
#reserve through the two pointer method 

s = "hello"
text = list(s)

p1 = 0
p2 = len(s) - 1 
temp =""

while p1 != p2:
     text[p1],text[p2] = text[p2],text[p1]
     p1 +=1
     p2 -=1

final = "".join(text)
print(final)
