### today i working on the quick sorting array 
import random

### quick sorting is nothing but each cycle choose 
### one pivot elements and arrange the larger elemnents to the left 
### larger elements to the right side of the array ....


### the code logic is most likely the merge sorting
def QuickSort(arr):
      subarr = arr[-1]
      leftArr = [i for i in subarr: if i > 5]
      return leftArr

result = QuickSort([9,2,5,1])

print(result)
