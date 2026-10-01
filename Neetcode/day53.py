#### hey hi today i am working on the subsequency of the pairs in the array

arr = [3,5,6,7]
target = 9
pointer = 0
reader = 0 
count  = 0


while pointer < len(arr):
        while reader < len(arr):
                    if arr[pointer]+arr[reader] <= target:
                            print(arr[pointer],arr[reader])
                            count +=1
                    reader +=1
        pointer +=1
        reader = pointer + 1

pointer = 0
reader = 0

print(count)

while pointer < len(arr):
        while reader < len(arr):
                    ar = arr[pointer:reader+1]
                    if min(arr)+max(arr) <= target:
                            count +=1
                    reader +=1
        pointer +=1
        reader = pointer + 1


print(count)


















