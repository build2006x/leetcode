### today i working on the quick sorting array 

import random

### quick sorting is nothing but each cycle choose 
### one pivot elements and arrange the larger elemnents to the left 
### larger elements to the right side of the array ....

### the code logic is most likely the merge sorting

### the main core logic is about choosing the pivot element and arange them left and right based on the comparsion ....
### quick sort 

def QuickSort(arr,left,right,count):
    if count == -1:
        count = len(arr)
    if count == 0:
        return [left,right]
    pivot_element = -1
    for i in range(0,len(arr)):
        if arr[i] < arr[pivot_element]:
            left.append(arr[i])
        else:
            right.append(arr[i])
    print([left,right])
    QuickSort(left,left,right,count=count-1)
    QuickSort(right,left,right,count=count-1)

result = QuickSort([3,41,2,1],left=[],right=[],count=-1)
print(result)