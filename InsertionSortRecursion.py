### this insertion sorting i need to change into the approach of recursion calls
### --- insertion --- sorting bascially checking i and i + 1 if same means swap them  
### -- example array = [3,1,34,2,4]
### -- 
arr = [3,1,34,2,4]

def SortingInsert(arr,p1,p2,count=None):
    if count == None:
        count = len(arr)
    if count == 0:
         return arr
    while p2 < len(arr):
        if arr[p2] < arr[p1]:
            arr[p1],arr[p2] = arr[p2],arr[p1]
        p1 +=1
        p2 +=1 
    
    return SortingInsert(arr,p1=0,p2=1,count=count-1)

result = SortingInsert([3,24,21,31,4],p1=0,p2=1,count=None)

print(result)




        
