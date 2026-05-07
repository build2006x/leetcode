### hi today i am working on the sum 
### called as the finding the longest array 

nums = [100, 4, 200, 1, 3, 2]  

arr = sorted(nums)
print(arr)
left = 0
right = 1
see = 0

while right < len(arr):     
     if arr[right] == arr[left]:
          right +=1
          left +=1
     elif arr[right] - arr[left] == 1:
          left +=1
          see +=1
          right +=1
     else:
           break

print(see+1)