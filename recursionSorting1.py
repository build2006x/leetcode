### bubblesorting using recursion 

### normally recursion is three part 

### first part contains -- recursion calls 
### second part contains -- define the base case to get stop to return the return 
### thrid part contains -- if condition true perform some action 

### this is basic structure of recursion algorithm 
#  point1 =0
#     point2 = point1 + 1 
#     for i in range(0,len(arr)//2):
#         while point2 < len(arr):
#             if arr[point1] > arr[point2]:
#                 arr[point1],arr[point2] = arr[point2],arr[point1]
#                 point1 +=1
#                 point2 +=1
#             point2 +=1
#             point1 +=1
#         point1 = 0 
#         point2 = point1 + 1

### now i am doing initailize the bubble using not focusing core things like how many times have to run a loop 


def BubbleSort(arr,count=None,p1=0,p2=1):
     if count == None:
        count = len(arr)
     if count == 1:
          return arr
     while p2 <= count-1:
          if arr[p1] > arr[p2]:
               arr[p1],arr[p2] = arr[p2],arr[p1]
          p1 +=1
          p2 +=1
     return BubbleSort(arr,count-1,p1=0,p2=1)
     
result = BubbleSort([92,41,4,1],count=None,p1=0,p2=1)
    
print(result)