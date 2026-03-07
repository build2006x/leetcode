### today 
### i am working on the plus one sum 

digits = [9]
main = digits[::-1]
p1 = 0

while p1 < len(digits):
     if main[p1] == 9:
           main[p1] = 0 
           main[p1+1] +=1  
     main[p1] +=1
     break

print(main[::-1])
 