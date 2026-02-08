## today i am working on merge sorting algorithm 
### -- we have to divide the array repeatedly and sort them and agin at last we have to merge them 

## three part of code are there like 
## first part --- is about spliting the array into less than 2 len of array each
 
## -- right and left part 

## -- check the left and right part and move the less one to the left array 

## -- at last move the remmaing elements which have been missed 


def mergeSort(arr):
    if len(arr) > 1:
        left_half = arr[:len(arr)//2]
        righ_half = arr[len(arr)//2:]

        mergeSort(left_half)
        mergeSort(righ_half)
        ### using recursion call we are repeadtly making array into the break of elements 
        ### until the every elements are breaks

        point1 = 0
        point2 = 0
        track = 0 #### this varaiable which is starting off index to put our values in arr by compare the left and right 
        print(f"leftarray:{left_half}")
        print(f"rightarray:{righ_half}")
        #### here we are setting the two pointer to go through and compare and sort the array 
        while point1 < len(left_half) and point2 < len(righ_half):
              if left_half[point1] < righ_half[point2]:
                    arr[track] = left_half[point1]
                    point1 +=1
              else:
                   arr[track] = righ_half[point2]
                   point2 +=1
              track +=1
       
        while point2 < len(righ_half):
                   arr[track]  = righ_half[point2]
                   point2 +=1
                   track +=1

        while point1 < len(left_half):
                    arr[track] = left_half[point1]
                    track +=1
                    point1 +=1

        return arr

result = mergeSort([5, 2, 4, 6, 1, 3])
             
print(result)
    
