## today approaching with reverse the vowels of a string 
## i how thinking like when pretty much having

##steps in progess to solve this sum 

#step : 1 like having the first point in the very start place 
#step : 2 having the another point in the very end place 
##step : 3 i will move the pointer towards each other until the end in the middle if find the vowels 
##at the each two pointer means i will swap them 
## important matter is like if the first pointer is not in vowels but point2 string is in vowels means i will dont move forwards and only point1 will be moved 

s = "IceCreAm"
main  =  list(s)

point1 = 0
point2 = len(s) - 1
vowels = set('aeiouAEIOU')

while point1 < point2:
      if main[point1] in vowels and main[point2] in vowels:
               main[point1],main[point2] = main[point2],main[point1]
               point1 +=1
               point2 -=1
      elif (main[point2] in  vowels and main[point1] not in vowels):
                 point1 +=1
      elif (main[point1] in  vowels and main[point2] not in vowels):
                    point2 -=1
      else:
              point1 +=1
              point2 -=1
print(main)    
result = "".join(main) 
print(result)