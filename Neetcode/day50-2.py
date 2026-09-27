####
#### hey hi today i am working on the 4sum problem

nums = [3,2,3,-3,1,0]
target = 3
result = []

arr = sorted(nums)
###[-3, 0, 1, 2, 3, 3]

###[-3,1,2,3] -- sol 


p1 = 0
p2 = p1 + 1


while p1 < p2:
        while arr[p1] >= 0:
                p1 +=1

        l = p2 + 1
        r = len(arr) -1   
        while p2 < len(nums) -2
        while l < r:  
                if arr[p1]+arr[p2]+arr[l]+arr[r] == target:
                            result.append([arr[p1],arr[p2],arr[l],arr[r]])
                            l +=1
                            r -=1
                elif  arr[p1]+arr[p2]+arr[l]+arr[r] < target:
                         l +=1
                else:
                         r -=1  
        p2 +=1
       

print(arr)
