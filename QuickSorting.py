### today i working on the quick sorting array 

import random

### quick sorting is nothing but each cycle choose 
### one pivot elements and arrange the larger elemnents to the left 
### larger elements to the right side of the array ....

### the code logic is most likely the merge sorting

### the main core logic is about choosing the pivot element and arange them left and right based on the comparsion ....
### quick sort 

# QuickSort is a divide-and-conquer algorithm:

"""
arr = [3,4,2,5]


pivot_element = arr[-1]

@@~~1

1st iteration 
left=[3,4,2]
pivot_element = [5]

@@~2
arr = [3,4,2]

pivot_element = [2]
left = [3]
right = [4]

this will continue until the array becomes the len(arr) <=1 
2sec iteration 
left 

"""

def QuickSort(arr):
    ### base case iteration runs until the len(arr) <=1
    if len(arr) <= 1:
        return arr
    
    ### intialize the pivot_element and subarray 
    pivot_element = arr[-1]
    left =[]
    Rigth = []

    for i in range(0,len(arr)-1): ### each iteration we know that the right most the last pivot element will be sorted
           if arr[i] < pivot_element:
                left.append(arr[i])
           else:
                 Rigth.append(arr[i])
  
    return QuickSort(left) + [pivot_element] + QuickSort(Rigth)
    
result = QuickSort([3,2,12,1,9])
print(result)

### the point is each iteration the pivot element position will be sorted in the list 