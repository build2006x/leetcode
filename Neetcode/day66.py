### hey hi today i am working on the 

list1 = [1,2,4]
list2 = [1,3,4]
length = 0


list3 = list1 + list2

if len(list3) % 2 == 0:
         length += len(list3) // 2
     
else:
        length += len(list3) //2  + 1


print(length)

l = 0
r = 1

while length !=0:
    while r < len(list3)-1:
            if list3[l] > list3[r]:
                    list3[l],list3[r] = list3[r],list3[l]
            l +=1
            r +=1 
    l = 0 
    r = 1
    length -=1

print(list3)
                        