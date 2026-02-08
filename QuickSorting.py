### today i working on the quick sorting array 
import random
### quick sorting is nothing but each cycle choose 
### one pivot elements and arrange the larger elemnents to the left 
### larger elements to the right side of the array ....

### the code logic is most likely the merge sorting

### the main core logic is about choosing the pivot element and arange them left and right based on the comparsion ....
### quick sort 


def QuickSort(arr,leftArr,rightArr):
    if len(leftArr) and len(rightArr) == 0:
        return arr
    PivotElement = -1
    


result = QuickSort([3,9,2,21,1],leftArr=[],rightArr=[])
print(result)