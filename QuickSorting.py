### today i working on the quick sorting array 
import random
### quick sorting is nothing but each cycle choose 
### one pivot elements and arrange the larger elemnents to the left 
### larger elements to the right side of the array ....

### the code logic is most likely the merge sorting

### the main core logic is about choosing the pivot element and arange them left and right based on the comparsion ....
### quick sort 


def QuickSort(arr,leftarr,rightarr,count):
    if count == 0:
           return [leftarr,rightarr]
    random_Element  = -1
    for i in range(len(arr)-2,-1,-1):
            if arr[i] < arr[random_Element]:
                    leftarr.append(arr[i])
            else:
                    rightarr.append(arr[i])
    return  QuickSort(arr,leftarr,rightarr,count=0)
    
result = QuickSort([9,8,3,2],leftarr=[],rightarr=[],count=1)
print(result)
