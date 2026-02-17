### today i am working on the consecutive ones in the array 

prices = [1, 1, 0, 1, 1, 1]



### basic apporach like i am thinking in the perspective of count the value and zero them and check the value greater means 
### take them orelse leave them 
track = 0
max_value = 0
count = 0

while track < len(prices):
      while track < len(prices):
            if prices[track] == 1:
                   count +=1 
            else:
                  break 
      track +=1
      max_value = max(max_value,count)
      count = 0
      if count == len(prices) - 1:
            break

print(max_value)

            