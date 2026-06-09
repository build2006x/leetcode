### today i am working on the subarray sums equals to k 

array = [3,1, 2, 4]
k=6

left = 0
right = 1
count = 1

while left < len(array):
    while right < len(array):
         if array[left:right+1] == k:
              print(array[left],array[right])
         right +=1
    right = left + 1



      
      
      


