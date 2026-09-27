####
#### hey hi today i am working on the 4sum problem

nums=[1,2,3,4]
target=10
arr = sorted(nums)
result = []

p1 = 0
p2 = p1 + 1

while p1 < len(nums)-3:

        l = p2 + 1
        r = len(arr) -1 
        print(p2,len(nums)-2)
        while p2 < len(nums) -2:
                while l < r:  
                        if arr[p1]+arr[p2]+arr[l]+arr[r] == target and sorted([arr[p1],arr[p2],arr[l],arr[r]]) not in result:
                                result.append(sorted([arr[p1],arr[p2],arr[l],arr[r]]))
                                l +=1
                                r -=1
                        elif  arr[p1]+arr[p2]+arr[l]+arr[r] < target:
                                l +=1
                        else:
                                r -=1  
                p2 +=1
                l = p2 + 1
                r = len(nums) -1 
        p1 +=1
        p2 = p1 +1 
       
print(result)
