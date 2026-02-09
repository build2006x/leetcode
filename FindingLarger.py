arr = [8, 10, 5, 7, 9]

### finding the large element--- 
Larger = 0

for i in range(0,len(arr)):
     if arr[i] > Larger:
          Larger = max(Larger,arr[i])

print(Larger)


### simple maintan a varaible to track the larger one number 
