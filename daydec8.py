#3sum 

##like finding of the sum of three number == 0 

Input = [-1,0,1,2,-1,-4]
     
#like my approach like keeping the two pointer in the last element in array and first pointer to first element 
#like keeping the first pointer as dyanamic moving the pointer and keeping the last two as static 

p1 = 0
p2  = len(Input) - 2
p3 = len(Input) - 1
final = []

while p1 < p2:
     if Input[p1]+Input[p2]+Input[p3] == 0:
          final.append([Input[p1],Input[p2],Input[p3]])
     p1 +=1

print(final)
          
      
