### returing the weather the string is palindorme or not 

string = "racecar"

p1 = 0
p2 = len(string) - 1

while p1!=p2:
     if string[p1] == string[p2]:
           p1 +=1
           p2 -=1
     else:print('false')

print('true')



























