### two point -- one is for iterating the list and another one for being static 
### we keep the array iterate through the entire array 
### get the small one and asing the unsorted part which keep stick to that first pointer 

arr = [1,3,4,2,5]

static = 0
min_value = 0 

while static < len(arr):
      for i in range(static+1,len(arr)):
              min_value = min(min_value,arr[i])
      arr[static] = min_value
      static +=1

print(arr)