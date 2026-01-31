#### it is simple sorting method of having two pointer of
### bubble sorting algorithm works by 
### repeatedly compare two elements and if need a swap means swap them and go
### do until arr are sorted 

## note that each iteration we have to 
## minus lenght of the arr beacuse last element will be in the array 

arr = [5, 4, 3, 2, 1]

count = 1
point1 = 0
point2 = point1 + 1

for i in range(0,len(arr)-count):
    while point2 <= len(arr)-1:    
        if arr[point1] > arr[point2]:
                arr[point1],arr[point2] = arr[point2],arr[point1] 
        point1 +=1
        point2 +=1
    point1 = 0
    point2 = point1 + 1
print(arr)


### now i am perfectly understanding the behind the sences of loigc of leaving the right most element in the each iteration 