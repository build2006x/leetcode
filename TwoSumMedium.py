### today i am trying to solve the perivously solved two sum with different 

### i am using the 

arr = [2,6,5,8,11]
target = 15
left = 0
right = 2

while left < len(arr)-1:
    while right < len(arr):
         if arr[left]+arr[right] == target:
               print('yes')
         right +=1
    left +=1
    right = left + 1


        
          