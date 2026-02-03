### bubblesorting using recursion 

### normally recursion is three part 

### first part contains -- recursion calls 
### second part contains -- define the base case to get stop to return the return 
### thrid part contains -- if condition true perform some action 

### this is basic structure of recursion algorithm 




def bubbleSort(arr):
    point1 =0
    point2 = point1 + 1 
    for i in range(0,len(arr)//2):
        while point2 < len(arr):
            if arr[point1] > arr[point2]:
                arr[point1],arr[point2] = arr[point2],arr[point1]
                point1 +=1
                point2 +=1
            point2 +=1
            point1 +=1
        point1 = 0 
        point2 = point1 + 1

    return arr

result = bubbleSort([2,3,1,45,32])

print(result)
