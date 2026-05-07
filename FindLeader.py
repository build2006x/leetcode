#### today i am working on the leetcode problem ---finding the leader 
arr = [10, 22, 12, 3, 0, 6]
reader = 0
pointer = 1
result = []

while reader < len(arr):
      while pointer < len(arr): 
         if arr[reader] > arr[pointer]:
             pointer +=1
         else:
              break 
      if pointer == len(arr):
           result.append(arr[reader])
      reader +=1
      pointer = reader + 1 
     

print(result)
            