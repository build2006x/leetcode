### today i am working on the consecutive ones in the array 

### basic apporach like i am thinking in the perspective of count the value and zero them and check the value greater means 
### take them orelse leave them 

arr = [1,1,1,1]

track = 0
count = 0 
valueMax = 0

for i in arr:
    if i == 1:
        count +=1
        valueMax  = max(valueMax,count)
    else:
        count =0
### how i am thiking like until the i will track will update if zero means goes to the update of the value and count to agin goes to the zero to start from 
print(valueMax)