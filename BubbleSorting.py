#### it is simple sorting method of having two pointer of

### bubble sorting algorithm works by 
### repeatedly compare two elements and if need a swap means swap them and go
### do until arr are sorted 
##note that each iteration we have to minus lenght of the arr beacuse last element will be in the array 

arr = [1, 3, 4, 2, 5]

point1 = 0
point2 = point1 + 1
count = 0
while point2 < len(arr):
        while count < len(arr):
            if arr[point1] > arr[point2]:
                    arr[point1],arr[point2] = arr[point2],arr[point1]
                    count +=1
            
        





