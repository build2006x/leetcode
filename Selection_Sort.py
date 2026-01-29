### two point -- one is for iterating the list and another one for being static 
### we keep the array iterate through the entire array 
### get the small one and asing the unsorted part which keep stick to that first pointer 

arr = [1,3,4,2,5]

static  = 0
### selection sorting is about parition of the two parts where unsorted and sorted ones in the given array 
while static < len(arr):
       min_value = static
       for i in range(static+1,len(arr)):
              if arr[static] > arr[i]:
                      min_value = i
       arr[static],arr[min_value] = arr[min_value],arr[static]
       static +=1

print(arr)


### the point is keep tracker of the values and min values holder from the start of array 

### logic -- where keeping two pointer - travler - Startindex - min_value 
### travler variable will start moving from the Startindex

### if large means get the index and swaps with the starting index
