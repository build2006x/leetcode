arr  = [2,7,5,11]

p1 = 0
p2 = len(arr) - 1
target = 9

while p1 < p2:
     if arr[p1] + arr[p2] == target:
          print('yes got it',[p1,p2])
     elif arr[p1] + arr[p2] > target:
          p2 -=1
     else:
          p1 +=1


          