### hey hi today i am working on the array 

nums=[10,20,30,5,10,50]
left = 0

start = 0
right = 1

max_sum = 0 

while right < len(nums):
        if nums[left] < nums[right]:
                left +=1
                right +=1
                max_sum = max(max_sum ,sum(nums[start:right]))
                print(nums[start:right+1])
        else:   
                print(nums[start:right+1])
                max_sum = max(max_sum ,sum(nums[start:right]))
                start = right
                end = start 
                left +=1
                right +=1
   
print(max_sum)