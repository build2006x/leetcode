### today i am working on the removing the duplicate 
### from the sorted array 

arr = [1,1,1,2,2,3,3,3,3,4,4]
##
actual = []
get_ritual = set(actual)
### adding the element to the set to avoid the duplicate
for i in arr:
    get_ritual.add(i)
get = list(get_ritual)
### here we are point to the arr 
point = 0
while point < len(get_ritual):
        arr[point] = get[point] 
        point +=1
while point < len(arr):
      arr[point] = 0
      point +=1

print(arr)


