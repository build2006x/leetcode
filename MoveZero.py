#### today i working on the moving the zero to the end leetcode sum 
# nums = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]


### first let me done with brute force 
# result = []
# count = 0
# for i in range(0,len(nums)):
#     if nums[i] != 0:
#         result.append(nums[i])
#     elif nums[i] == 0:
#         count +=1

# for j in range(0,count):
#     result.append(0)

# print(result)


#### above code is sovled by the brute force 
### now we have to think for the optimal approach 

#### --- two pointer method ...

arr = [4, 0, 5, 0, 0, 6]

start = 0
track = 1

while start < len(arr):
      while track < len(arr):
            if arr[track] !=0:
                if arr[start] == 0:
                  arr[start],arr[track] = arr[track],arr[start]
                  break
                else:
                     arr[start+1],arr[track] = arr[track],arr[start+1] 
                     break
            track +=1
      start += 1
      track = start + 1

print(arr) 