### i wanted to find the common element 

n = 5
m = 5 
arr1 = [1,2,3,4,5]  
arr2 = [2,3,4,4,5]

setMap  = set()

for i in range(0,len(arr1)):
    setMap.add(arr1[i])

for j in range(0,len(arr2)):
    setMap.add(arr2[i])

print(setMap)