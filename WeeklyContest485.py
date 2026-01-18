### today contest i am trying to solve at least two problem 
###

s = "i3"
ar1 = ['a','e','i','o','u']
ar2 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
point = 0
c = 0
v = 0
while point < len(s):
    if s[point] in ar1:
       v +=1
       point  +=1
    elif s[point] in ar2:
        c +=1
        point +=1
    else:
        point +=1


if c == 0:
    print('0')
else:
    print(v//c)
