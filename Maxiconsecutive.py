### today i am working on the consecutive ones in the array 

### basic apporach like i am thinking in the perspective of count the value and zero them and check the value greater means 
### take them orelse leave them 

prices = [1, 1, 0, 1, 1, 1]

track = 0
point = 0
value = 0

while point < len(prices):
      if prices[point] == 1:
             track +=1
             point +=1
      else:
           value = max(value,track)
      point +=1

print(value)
       
      
