###today i am working on binnary search 
##for further working on dsa 
## binnary searching on array 

nums = [-1,0,3,5,9,12]
target = 9

right = len(nums) - 1
left = 0
mid = 0

while left <= right:
     mid = (left + right)//2
     if nums[mid] == target:
          print('yes we got')
          break
     elif nums[mid] < target:
          left +=1
     else:
          right -=1


 