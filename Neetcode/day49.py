#### hey hi today i am working on the 3 sum question optimal way of solving approach --- two pointer 

nums = [0,0,0]

arr = sorted(nums)
pointer = 0
result = []


### how the things works 

## 01 -- we sorted the array to keep high and low point to find out the pairs 
## 02 -- by the simple math formula we used to think -- negative = consent two postive integer 
### 

while pointer < len(arr)-2:
        while arr[pointer] > 0 and arr[pointer] == arr[pointer-1]:
                pointer +=1
        l = pointer + 1 
        r = len(arr) - 1

        while l < r:
                if arr[l]+arr[r] == abs(arr[pointer]):
                        result.append([arr[pointer],arr[l],arr[r]])
                        while l < r and arr[l] != arr[l+1]:
                                 l +=1
                        while l < r and arr[l] != arr[r-1]:
                                r -=1
                        l +=1
                        r -=1
                elif arr[l]+arr[r] < abs(arr[pointer]):
                         l +=1

                else:
                        r -=1
        pointer +=1

print(result)
                                  
        
                 